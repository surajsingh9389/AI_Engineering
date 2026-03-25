import faiss 
import numpy as np
from google import genai
import os
from dotenv import load_dotenv


# 1. Load your .env file
load_dotenv()

# 2. Initialize the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_embedding(text):
    
    result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
    ) 

    return np.array(result.embeddings[0].values)

sentences = [
 "I love machine learning",
 "Python is great for backend",
 "AI is the future",
 "Football is a great sport"
]

sample = get_embedding("test")
# dimension of embedding
d = len(sample)

# Index is the entire container or database that holds all your vectors 
index = faiss.IndexFlatL2(d)

sentences_embeddings = [get_embedding(v) for v in sentences]

sentences_embeddings = [v/np.linalg.norm(v) for v in sentences_embeddings]

# FAISS is built for extreme speed. To be that fast, it requires float32 (slightly less precision, but uses half the memory).
embeddings = np.array(sentences_embeddings).astype('float32')

index.add(embeddings)

query = input("Enter query: ")
k = int(input("Enter top matches you want: "))

query_embeddings = get_embedding(query)
query_embeddings = query_embeddings/np.linalg.norm(query_embeddings)

query = np.array([query_embeddings]).astype('float32')

distances, indices = index.search(query, k)

print(indices)
print(distances)

for i in indices[0]:
    if i != -1: # FAISS returns -1 if it can't find enough matches
        print(f"Match: {sentences[i]}")



# Faiss is a library, not a full-fledged database system. Faiss (The Engine): Provides the raw power to perform high-speed mathematical searches and indexing. does not provide metadata storage, Real CRUD, Built-in Persistence, Multi-user Access.

# Use Faiss (Library) if you are building a prototype, conducting research, or have a static dataset where you want maximum speed with minimal overhead.