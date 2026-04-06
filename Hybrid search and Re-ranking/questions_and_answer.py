# Q1. In your current system (FAISS + embeddings), How does similarity search actually work?

# ans = similarity search use mathematical operations between vectors check how similar are they, the top-k similar shunks means it refers to this k number of results that have the highest similarity scores to the query, We are comparing the numerical representations (embeddings) of meaning between the user query vector and the stored data in a high-dimensional vector space.


# Q2 (Limitation Awareness)
# Vector search is powerful, but not perfect.
# 👉 Can you give 2 real-world cases where vector search alone might fail to retrieve the correct information?

# ans = if fails when - 
# 1. you need to match specific Id, product codes, or rare technical terms where close is not good enough, 2. if your query have negation keyword it ignore them and provide the oposite result.

# Q3 (Keyword vs Semantic Thinking)

# Imagine this query:

# "What is the revenue of Apple in 2023?"

# 👉 Which method would perform better and why:

# Keyword Search (BM25)
# Vector Search (Embeddings)

# Now consider this query:

# "How much money did Apple make last year?"

# ans= for the first query the keyword search perform good because it use keyword like 2023 and revenue to match the same result, and for query 2 the vector search is good because not much keyword so we can use semantic meaning to find answer.


# Q4 (System Design Thinking - Intermediate)

# You now have 2 retrieval systems:

# BM25 (keyword-based)
# FAISS (vector-based)

# 👉 How would you combine them?

# Run both separately?
# Merge results?
# Which one do you trust more?

# Explain your approach.

# ans= first run BM25 to find the exact keyword chunks which contains the information and from those chunsk check which are more similar to the query, BM25 use keyword search so it wil give more accurate result compare to vector base search.

# ans2 = Better industry approach:

# Run both independently
# Combine results using techniques like:
# Score fusion
# Reciprocal Rank Fusion (RRF)

# Q5 (Real-world Engineering - Advanced)

# Let’s say your retriever returns 20 chunks.

# 👉 Why might we still need a re-ranking step using an LLM or cross-encoder?

# What problem does re-ranking solve that retrieval doesn’t?

# ans= to find more accurate and similar result as per query we use re-rank the chunks again to find more suitable answer.

#ans2= Retrieval (FAISS/BM25):

# Fast
# Approximate
# Works at chunk level

# 👉 Re-ranking (Cross-encoder / LLM):

# Slow but very accurate
# Looks at query + chunk together
# Understands context deeply

# 💡 Key idea:

# Retrieval finds candidates
# Re-ranking finds the best answer