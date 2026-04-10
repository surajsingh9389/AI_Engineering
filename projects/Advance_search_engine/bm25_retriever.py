from rank_bm25 import BM25Okapi

class Bm25Retriever:
    def __init__(self, docs):
        self.docs = docs
        
        # BM25 expects a list of lists (each list contains words)
        self.tokenized_corpus = [doc.lower().split() for doc in self.docs]
        
        # Initialize the BM25 object
        self.bm25 = BM25Okapi(self.tokenized_corpus)   
    
    def get_top_k(self, query, k=3):
        
        # Tokenize your query
        tokenized_query = query.lower().split()
        
        return self.bm25.get_top_n(tokenized_query, self.docs, n=k)