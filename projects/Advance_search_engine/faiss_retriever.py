import faiss

class FaissRetriever:
    def __init__(self, embeddings_docs, docs):
        
        self.docs = docs
        
        # normalize embedding_docs
        faiss.normalize_L2(embeddings_docs)
        
        self.d = embeddings_docs.shape[1]

        # Initialize the index 
        self.index = faiss.IndexFlatIP(self.d)
        
        # Store Embeddings 
        self.index.add(embeddings_docs)
        
    def retrieve_top_k(self, embedding_query, k=3):
        
        # normalize query 
        faiss.normalize_L2(embedding_query)
        
        # Search query on docs 
        distance, indices = self.index.search(embedding_query, k)
        
        return [self.docs[i] for i in indices[0]]
        
        
        
    
    