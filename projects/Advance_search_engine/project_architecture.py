# User Query
#    ↓
# BM25 Retriever (keywords)
#    ↓
# FAISS Retriever (semantic)
#    ↓
# RRF Fusion (combine signals)
#    ↓
# Cross-Encoder (deep ranking)
#    ↓
# Top-K Documents