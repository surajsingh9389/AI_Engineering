# Q1. Why is storing embeddings in a file (pickle) still not scalable?
# Ans = Pickle is not scalable because it does not support efficient search, indexing, or updates for large vector datasets. still do linear scan -> O(n), because fo no indexing, cannot do nearest neighbor search efficiently, memmory issues Loads entire file into RAM, NO concurrency and scaling.

# Q2. What is the difference between: Exact search vs Approximate search (ANN)
# Ans = Excat Search, Compares query with every vector, 100% correct nearest neighbor. O(n*m).
# ANN Does not check all vectors, instead Uses smart structure to find "almost nearest" 95-99% accuracy, O(log n) or sublinear.


# Q3. Why do companies NOT compute embeddings at query time for documents?
# Ans = Because documents are static and expensive to embed, so computing embeddings repeatedly is inefficient and increases latency and cost. Precompute once → store in vector DB. Only embed user query at runtime.

# -----------------------------------------------------------

# Q1. Why does FAISS require float32 instead of default NumPy types?
# Ans: default numpy types are in float64 high precison in which a number require 8 byte space which which can be more accurate but takes more space of ram and time. but in float32 it takes only 4 byte which is half as compare to float64 thats it takes more data and provide more speed, also the FAISS library is buitl in c++ if in FAISS we did not provide float32 precison number it will throw the error.

# Ans2. FAISS uses float32 because it is optimized for speed and memory efficiency at scale, and its underlying C++ implementation is designed to work with float32 arrays.
# float32 → better CPU cache usage → faster distance calculations
# FAISS does NOT accept float64 → you must convert to float32
# float32 = best tradeoff between speed, memory, and accuracy


#Q2. What happens if you DON’T normalize vectors but still use IndexFlatIP?
# Ans = in IndexFlatIP, IP means inner product, it use dot product to calculate simmilarity between two vectore after nomalizaton the vector become unit length the dot product two nomalize vector is always scale on -1 to 1 that way we can easily find the similarity between two vectors, but if we not normalize the vectors if one vector magnitude is greater than other vector the dot product of two vectors also high even though they are not similar.

# Ans2. Without normalization, inner product (dot product) is influenced by both direction and magnitude, so vectors with larger magnitudes may appear more similar even if their meanings differ.

# Normalization ensures similarity = meaning, not size

# Q3. Why is FAISS faster than your Python loop?
# Ans = loop and in FAISS IndexFlatL2 aslos check all vectors but FAISS is fast because- FAISS → low-level optimized code, Python → slow loops, faiss computes many distances in parallel. Cache-friendly layout -> faster reads, same algorithm, but much faster execution.

# Ans2. FAISS is faster because it uses optimized C++ code, vectorized computations, and efficient memory usage, even though IndexFlatIP still performs exact search over all vectors.