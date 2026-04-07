from rank_bm25 import BM25Okapi
import faiss

# Using Bm25 the top matching

docs = [
  "Samsung return policy is 10 days",
  "Refunds are processed within 5 days",
  "iPhone 15 refund policy is 7 days"
]

# BM25 expects a list of lists (each list contains words)
tokenized_corpus = [doc.lower().split() for doc in docs]

# Initialize the BM25 object
bm25 = BM25Okapi(tokenized_corpus)

# Tokenize your query

query = "iPhone refund".lower().split()

# Get scores or the top results
doc_scores = bm25.get_scores(query)
top_n = bm25.get_top_n(query, docs, n=3)

print(f"Scores: {doc_scores}")
print(f"Best Match: {top_n}")


# Using Faiss the top matching 

