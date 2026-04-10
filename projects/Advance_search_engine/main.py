from bm25_retriever import Bm25Retriever
from faiss_retriever import FaissRetriever
from hybrid_retrieval import HybridRetriever
from re_rank import ReRanker
from generate_embedding import Embedder
from retrieval_pipeline import RetrievalPipeline
import numpy as np

docs = [
  "Samsung return policy is 10 days",
  "Refunds are processed within 5 days",
  "iPhone 15 refund policy is 7 days"
]

query = "What is the return policy for an Apple iPhone?"

embedder = Embedder()

# document, query Embedding 
embedding_docs = np.array(embedder.get_embedding(docs)).astype('float32')

# BM25 Retriever Layer
bm25_model = Bm25Retriever(docs)

# faiss Retriever Layer
faiss_model = FaissRetriever(embedding_docs, docs)

# Hybrid model rrf fusion Layer
hybrid_model = HybridRetriever()

# Re rank the hybrid results coress encoder Layer 
re_rank_model = ReRanker()

# combine single pipeline 
pipeline = RetrievalPipeline(bm25_model, faiss_model, embedder, hybrid_model, re_rank_model)

res = pipeline.run(query)
print(res)
