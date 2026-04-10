class HybridRetriever:
    def __init__(self, k=60):
        self.k = k
        
    def rrf(self, bm25_results, faiss_results):
        scores = {}
        
        # BM25(keyword search) contribution
        for rank, doc in enumerate(bm25_results, 1):
            scores[doc] = scores.get(doc, 0) + 1/(rank+self.k)
        
        # faiss(Semantic search) contribution
        for rank, doc in enumerate(faiss_results, 1):
            scores[doc] = scores.get(doc, 0) + 1/(rank + self.k)
            
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)