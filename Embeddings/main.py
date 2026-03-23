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
