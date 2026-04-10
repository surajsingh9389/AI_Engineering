from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        # 1. Load a model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def get_embedding(self, text):    
        return self.model.encode(text)
    