# Q1. Why is storing embeddings in a file (pickle) still not scalable?
# Ans = Pickle is not scalable because it does not support efficient search, indexing, or updates for large vector datasets. still do linear scan -> O(n), because fo no indexing, cannot do nearest neighbor search efficiently, memmory issues Loads entire file into RAM, NO concurrency and scaling.

# Q2. What is the difference between: Exact search vs Approximate search (ANN)
# Ans = Excat Search, Compares query with every vector, 100% correct nearest neighbor. O(n*m).
# ANN Does not check all vectors, instead Uses smart structure to find "almost nearest" 95-99% accuracy, O(log n) or sublinear.


# Q3. Why do companies NOT compute embeddings at query time for documents?
# Ans = Because documents are static and expensive to embed, so computing embeddings repeatedly is inefficient and increases latency and cost. Precompute once → store in vector DB. Only embed user query at runtime.