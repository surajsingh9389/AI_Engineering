from rank_bm25 import BM25Okapi
import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np

# ------------ Using Bm25 the top matching ---------------

docs = [
  "Samsung return policy is 10 days",
  "Refunds are processed within 5 days",
  "iPhone 15 refund policy is 7 days"
]

query = "What is the return policy for an Apple iPhone?"

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

print(f"Hybrid Results: {hybrid_results}")

# ------------- Re-Ranking ----------------

# Convert into pairs(query, retrieve_docs)
pairs = [(query, doc) for doc, _ in hybrid_results]

print(f"Query + docs: {pairs}")

# Load model 
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# calculate scores for re-ranking 
scores = model.predict(pairs)

sorted_docs = sorted(zip([doc for doc, _ in hybrid_results], scores), key=lambda x: x[1], reverse=True)

print(f"After Re-Ranking docs and scores: {sorted_docs}")

