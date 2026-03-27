import numpy as np
import os
from google import genai
import faiss
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embeddings(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    
    return np.array(result.embeddings[0].values).astype('float32')

def safe_normalize(v):
    magnitude = np.linalg.norm(v)
    if magnitude == 0:
        return v
    return v/magnitude

def generate_answer(context, query):
    prompt = f"""
    Answer the question using ONLY the context below.
    
    Context: 
    {context}
    
    Question:
    {query}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text

documents = [
    "Machine learning is a subset of AI.",
    "Python is widely used for backend development.",
    "FAISS is used for fast similarity search.",
    "RAG combines retrieval and generation.",
    "Neural networks are inspired by the human brain."
]

raw_embeddings = [get_embeddings(v) for v in documents]

nomalize_embeddings = [safe_normalize(v) for v in raw_embeddings]

embeddings_documents = np.array(nomalize_embeddings).astype('float32')

d = embeddings_documents.shape[1]

index = faiss.IndexFlatIP(d)

index.add(embeddings_documents)

query = input("Ask Something: ")
k = 2

embed_query = get_embeddings(query)
embed_query = safe_normalize(embed_query)
embed_query = np.array([embed_query]).astype("float32")

distance, indices = index.search(embed_query, k)

retrieved_docs = [documents[i] for i in indices[0]]

context = '\n'.join(retrieved_docs)
print(context)

answer = generate_answer(context, query)
print(answer)



