from rank_bm25 import BM25Okapi
import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder
from huggingface_hub import InferenceClient
import os
import numpy as np

# ------------ Using Bm25 the top matching ---------------

docs = [
  "Samsung return policy is 10 days",
  "Refunds are processed within 5 days",
  "iPhone 15 refund policy is 7 days",
  "The Amazon river is the largest by discharge volume.",
  "Amazon.com is a leading e-commerce company."
]

query = "How long does iPhone refund take?"
# query = "what is Amazon?"

# BM25 expects a list of lists (each list contains words)
tokenized_corpus = [doc.lower().split() for doc in docs]

# Initialize the BM25 object
bm25 = BM25Okapi(tokenized_corpus)

# Tokenize your query
tokenized_query = query.lower().split()

# Get scores or the top results
doc_scores = bm25.get_scores(tokenized_query)
top_n = bm25.get_top_n(tokenized_query, docs, n=3)

bm25_results = top_n
# print(bm25_results)

# print(f"Scores: {doc_scores}")
# print(f"Best Match: {top_n}")


# --------------- Using Faiss the top matching ----------------

# 1. Load a model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embedding_docs = model.encode(docs)
embedding_query = model.encode(query)

embedding_docs = np.array(embedding_docs).astype('float32')
embedding_query = np.array([embedding_query]).astype('float32')

# normalize Embeddings 
faiss.normalize_L2(embedding_docs)
faiss.normalize_L2(embedding_query)

d = embedding_docs.shape[1]

index = faiss.IndexFlatIP(d)

index.add(embedding_docs)
k = 3

distance, indices= index.search(embedding_query, k)

faiss_results = [docs[i] for i in indices[0]]

# print(faiss_results)

# for j, i in enumerate(indices[0]):
#   print(f"score: {distance[0][j]}, sentence: {docs[i]}")


# ------------- RRf algorithm ----------------

def rrf(bm25_results, faiss_results, k=60):
  scores={}
  
  # BM25 contribution
  for rank, doc in enumerate(bm25_results, 1):
    scores[doc] = scores.get(doc, 0) + 1/(rank+k)
    
  # Faiss contribution
  for rank, doc in enumerate(faiss_results, 1):
    scores[doc] = scores.get(doc, 0) + 1/(rank+k)
    
  return sorted(scores.items(), key=lambda item: item[1], reverse=True)


hybrid_results = rrf(bm25_results, faiss_results)

# print(f"Hybrid Results: {hybrid_results}")

# ------------- Re-Ranking ----------------

# Convert into pairs(query, retrieve_docs)
pairs = [(query, doc) for doc, _ in hybrid_results]

# print(f"Query + docs: {pairs}")

# Load model 
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# calculate scores for re-ranking 
scores = model.predict(pairs)

sorted_docs = sorted(zip([doc for doc, _ in hybrid_results], scores), key=lambda x: x[1], reverse=True)

print(f"After Re-Ranking docs and scores: {sorted_docs}")


def build_prompt(context):
  
  prompt = f"""
You are a strict question-answering assistant.

Rules:
1. Answer ONLY using the provided context.
2. Do NOT use any external knowledge.
3. The answer must be explicitly stated in a SINGLE sentence from the context.
4. Do NOT combine information from multiple sentences.
5. If the answer is not explicitly present, respond with EXACTLY:
   "I don't know"
6. Do NOT explain your answer.
7. Do NOT add any extra text.

------

Example 1:
Context: iPhone refund policy is 7 days
Question: What is iPhone refund policy?
Answer: iPhone refund policy is 7 days

Example 2:
Context: Refunds are processed in 5 days
Question: What is the price of iPhone?
Answer: I don't know

Example 3:
Context:
Refunds are processed within 5 days
iPhone 15 refund policy is 7 days

Question:
How long does iPhone refund take?

Answer:
I don't know

------

Context:
{context}
"""
    
  return prompt

# Retrieve context 
retrieve_docs = [doc for doc, _ in sorted_docs]
context = "\n".join(retrieve_docs)

# Generate prompt 
prompt = build_prompt(context)


# Your Read Token from: https://huggingface.co
HF_TOKEN = os.getenv("TOKEN")

# Initialize the client with your API token
client = InferenceClient(api_key=HF_TOKEN)

def generate_rag_answer(user_query, prompt):
    # The 'best way' is using the OpenAI-compatible chat interface
    model_id = "deepseek-ai/DeepSeek-V3" 
    
    messages = [
        {
            "role": "system", 
            "content": prompt
        },
        {
            "role": "user", 
            "content": user_query
        }
    ]

    response = client.chat.completions.create(
        model=model_id,
        messages=messages,
        max_tokens=100,
        temperature=0.0, # Lower temperature is better for factual RAG
        stop=["\n"]
    )
    
    return response.choices[0].message.content


answer = generate_rag_answer(query, prompt)
print(f"Generated Answer:\n{answer}")