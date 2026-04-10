import numpy as np

class RetrievalPipeline:
    def __init__(self, bm25, faiss, embedder, hybrid, reranker):
        self.bm25 = bm25
        self.faiss = faiss
        self.embedder = embedder
        self.hybrid = hybrid
        self.reranker = reranker

    def run(self, query):
        bm25_res = self.bm25.get_top_k(query)
        embedding_query = np.array([self.embedder.get_embedding(query)]).astype('float32')
        faiss_res = self.faiss.retrieve_top_k(embedding_query)        
        hybrid_res = self.hybrid.rrf(bm25_res, faiss_res)
        final_res = self.reranker.re_rank(query, hybrid_res)
        return final_res