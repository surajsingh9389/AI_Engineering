from sentence_transformers import CrossEncoder

class ReRanker:
    def __init__(self):
        # Load model 
        self.model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        
    def re_rank(self, query, docs, k=3):
        
        doc_list = [doc for doc, _ in docs]
        
        # pair the query, docs 
        pairs = [(query, doc) for doc in doc_list]
        
        # calculate scores for re-ranking
        scores = self.model.predict(pairs)
                
        # re rank docs based on re-ranking scores 
        res = sorted(zip(doc_list, scores), key=lambda x: x[1], reverse=True)
    
        return res[:k]