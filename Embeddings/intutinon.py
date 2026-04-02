# Embeddings in AI are numerical representations of data—such as text, images, or audio—converted into vectors (lists of numbers) that capture their semantic meaning and relationships.

# text -> meaning -> numbers

# ----------------------------------

# Example - 

# "I love AI"
# [0.23, -0.91, 0.44]

# -----------------------------------------------------

# why needed - because computers understand numbers not text

# -----------------------------

# where use - 

# semantic search
# RAG systems
# chatbots
# recommendation systems

# -----------------------------------------------

# Which chunk will produce BETTER retrieval and WHY?

# Chunk A:
# "Refund allowed within 7 days."

# Chunk B:
# "This document explains the refund policy. Refund allowed within 7 days after purchase."

# ans = Chunk B performs better not because it is larger, but because it provides relevant contextual information (“refund policy”) along with the key fact. This helps the embedding model better align with user queries that include both intent and context, improving retrieval accuracy.

# Q. rewrite it to make embedding stronger for retrieval.

# "Users can reset their password using email verification."

# ans = i provide these options.
# 1. Password reset: "Users can reset their password using email verification."
# 2. Forgot Password: "Users can reset their password using email verification."


# Q. Why should we NOT embed query and document in exactly the same way? 
# ans = Queries and documents serve different purposes.
# A query represents intent and is usually short, while a document represents knowledge and is more detailed.

# If both are embedded in the same way:

# Queries may lack enough context to match rich documents effectively
# Documents may contain too much information, diluting relevance

# This mismatch leads to poor similarity scoring and weaker retrieval performance.