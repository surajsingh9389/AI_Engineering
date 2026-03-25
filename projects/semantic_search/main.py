import numpy as np
import faiss
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

    return np.array(result.embeddings[0].values).astype('float32')


# def get_top_k(scores, k):
#     if k == 0 or k > len(scores): 
#         return []
    
#     new_scores = heapq.nlargest(k, enumerate(scores), key=lambda x: x[1])
    
#     return new_scores 

def safe_normalize(v):
    magnitude = np.linalg.norm(v)
    if magnitude == 0:
        return v
    return v/magnitude
    
   

# def semantic_search(query, normalize_embeddings, sentences, k):
    
#     embedding_query = get_embedding(query)
#     normalize_query = safe_normalize(embedding_query)
    
#     # Similarity 
#     scores = [np.dot(normalize_query, v) for v in normalize_embeddings]

#     top_matches = get_top_k(scores, k)
    
#     return [(sentences[i], score) for i, score in top_matches]



sentences = [
 "I love machine learning",
 "Python is great for backend",
 "AI is the future",
 "Football is a great sport"
]

# CACHE_FILE = r"projects\semantic_search\embeddings.pkl"

# # API Call Cost Optimization (Caching)

# if os.path.exists(CACHE_FILE):
#     print("Loading embeddings from cache...")
#     with open(CACHE_FILE, "rb") as f:
#         normalized_embeddings = pickle.load(f)
        
# else: 
#     print("Fetching embeddings from Gemini...")
#     raw_embeddings = [get_embedding(v) for v in sentences]
#     # Avoid Normalizing Every Query (Pre-normalization)
#     normalized_embeddings = [safe_normalize(v) for v in raw_embeddings]
    
#     # This will create the folders if they don't exist
#     os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    
#     with open(CACHE_FILE, "wb") as f:
#         pickle.dump(normalized_embeddings, f)


# Sentences embedding
raw_embeddings = [get_embedding(v) for v in sentences]

# Sentences Normalization 
normalized_embeddings = [safe_normalize(v) for v in raw_embeddings]

# for extreme speed, float32 type slightly less precision(compare to 64), but uses half the memory. Each number takes 4 bytes.
embeddings_matrix = np.array(normalized_embeddings).astype('float32')

# dimension of embedding
d = embeddings_matrix.shape[1]  # .shape -> (row, cols)

# container or database that holds all your vectors 
index = faiss.IndexFlatIP(d) # Inner Product (best for cosine)

# Add embeddigs to the database 
index.add(embeddings_matrix)

query = input("Enter your search query: ")
k = int(input("How many top matches you want?: "))

query_embedding = get_embedding(query)
print(query_embedding)

normalized_query = safe_normalize(query_embedding)

normalized_query = np.array([normalized_query]).astype('float32')

distances, indices = index.search(normalized_query, k)

for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {sentences[idx]} (score: {distances[0][i]:.4f})")


# Note: Why indexFaltIP, IP = Inner product = dot product, since we normalized vectors dot product = cosine similarity.

# So : FAISS + normalization = cosine similarity search 