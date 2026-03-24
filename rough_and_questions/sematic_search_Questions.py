# -------------------------------------------------

# Q1. Why do we use cosine similarity instead of direct comparison.
# Ans = if use direct comparison they compare by there weight or magnitude not by there direction, on the other hand cosine similarity compare using direction. 

# Q2. time complexity fo semantic search
# Ans = let sentence_vectors is nxm based on this 
#     compute_cosine_similarity is O(m)
#     calculate_scores is O(nxm)
#     find_best_score_idx is O(n) 
    
#     so the time complexity of semantic search is O(nxm) + O(n)

# Q3. How can this become slow with 1 million vectors?
# store normaalized vectors avoid recomputing magnitude 

# ----------------------------------------------

# -------------------------------------------------

# Q1
# Why do embeddings usually have hundreds of dimensions (e.g., 768, 1536)?

# Ans -  each dimension captures a different feature of meaning.
 
# dimension 1 → "technology"
# dimension 2 → "emotion"
# dimension 3 → "sports"
# ...  

# More dimensions = richer meaning representation 


# Q2
# What happens if two completely different sentences have similar vectors?

# Ans - model limitaion / imperfect embedding space , this i called semantic collision(same direction but not similar meaning). real-world impact Wrong search results and incorrect chatbot answers. for solve this problem we use better models, reranking, RAG pipelines.

# Q3
# Why is storing vectors in a normal database (MongoDB) inefficient?

# Ans - MongoDB cannot perform fast vector similarity search. cosine similarity requires scanning ALL vectors -> O(n) very slow. soln - specialized vector DBs, FAISS, pinecone, Chroma, they use approximate nearest neighbor (ANN), make search O(log n) instead of O(n)

# -----------------------------------------------------------------

# Q1. what is the difference between search by keywords vs serch by embedding

# Ans = Keyword → Matches exact words, Embedding → Matches meaning (semantic similarity)

# Q2. Why is cosine similarity preferred over dot product alone?

# Ans = if one vector magnitude is larger comapare to other if do there dot product the dot product become high even though the two vector have not similar meaning, but in cosine similarity we first normalize the vector so there magnitude become 1, because of this the focuse entirely shifts to the direction of meaning.

# Dot product → magnitude + direction
# Cosine → only direction (meaning)

# Q3
# What is one limitation of your current semantic search system?
# Ans = the two sentence which are not similar but there vectors are same can cause problem in my current semantic search system.

# ------------------------------------------


# Q1
# Why is O(n log k) better than O(n log n) in your case?
# Ans = O(n log n) sorts the entire list, O(n log n) sorts the entire list

# Q2
# What will happen if we normalize all vectors before storing them?
# Ans - remove the number of operation require to calculate cosine similarity which improve the time complexity.

# Q3
# If dataset becomes 1 million vectors, what breaks in your system?

# Ans - comparing in 1 million vectors linearly takes lots of time, the system stuck on comparing the vector

# ------------------------

# Q1. Why are embeddings 1536 dimensions instead of 3?
# Ans = the dimensions represent the different meaning level, means the sentence contain different attribute of meaning thats there are that many dimension 

# Q2. Why is API-based embedding slower than your previous NumPy system?

# Ans = Main reason = network + model computation, Api call over internet, Response time

# NumPy → local + simple math (fast)
# API → remote + deep model (slow but meaningful)


# Q3. What happens if you don’t normalize embeddings?
# Ans = Dot product gets influenced by magnitude, not just meaning, Normalization ensures similarity depends only on direction (meaning)