# Task1: 
from google import genai
import os
from dotenv import load_dotenv

# 1. Load your .env file
load_dotenv()

# 2. Initialize the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. Use the updated model name
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="I love machine learning"
) 

# 4. Access the embedding values correctly
embedding = result.embeddings[0].values

print(f"Vector Length: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")


# Task2  and Task 3:
import numpy as np
import heapq
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


def get_top_k(scores, k):
    if k == 0 or k > len(scores): 
        return []
    
    new_scores = heapq.nlargest(k, enumerate(scores), key=lambda x: x[1])
    
    return new_scores 
   

def semantic_search(query_embedding, sentence_embeddings, sentences, k):
    
    # Normalize 
    normalize_sentence = [v /np.linalg.norm(v) for v in sentence_embeddings]
    normalize_query = query_embedding/np.linalg.norm(query_embedding)
    
    # Similarity 
    scores = [np.dot(normalize_query, v) for v in normalize_sentence]

    top_matches = get_top_k(scores, k)
    
    return [(sentences[i], score) for i, score in top_matches]



sentences = [
 "I love machine learning",
 "Python is great for backend",
 "AI is the future",
 "Football is a great sport"
]

query = "I love Ai"

k = int(input("How many top matches you want?: "))

# Convert all sentences -> embeddings 
sentence_embeddings = [get_embedding(s) for s in sentences]

# Query embedding 
query_embedding = get_embedding(query)
        
top_matches = semantic_search(query_embedding, sentence_embeddings, sentences, k)

print(top_matches)


# ------------------------

# Q1. Why are embeddings 1536 dimensions instead of 3?
# Ans = the dimensions represent the different meaning level, means the sentence contain different attribute of meaning thats there are that many dimension 

# Q2. Why is API-based embedding slower than your previous NumPy system?

# Ans = API_based compute many dimension meaning there are lots of dimension in api-based vector in which each represents diffrent meaning, computing these meaning to dimensions takes times where in previous system we are doing this randomly also vector size is also small.


# Q3. What happens if you don’t normalize embeddings?
# Ans = there can be one vector which magnitude is greater to other vector the dot product of these vectors become very large even there meaning are not same by normalizing the vectors we scale them so there magniute become 1. because of this the dot product of two vectors always in the range of -1 to 1.

# Note - also istead of openai i am using googl genai for embedding 