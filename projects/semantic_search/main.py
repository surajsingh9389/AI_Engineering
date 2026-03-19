import numpy as np

def compute_cosine_similarity(a, b):
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    dot_product = np.dot(a, b)
    
    return dot_product/(magnitude_a*magnitude_b)

def find_best_score_idx(scores):
    max_score_idx = 0  
    
    for i, score in enumerate(scores, 0):
        if(score>scores[max_score_idx]):
            max_score_idx = i
    
    return max_score_idx        
    
 
def calculate_scores(query_vector, sentence_vectors):
    scores = []
    for vector in sentence_vectors:
        current_vector_cs = compute_cosine_similarity(query_vector, vector)
        
        scores.append(current_vector_cs)
        
    return scores    
    
    

def semantic_search(query_vector, sentence_vectors, sentences):
    scores =  calculate_scores(query_vector, sentence_vectors)

    best_matching_score_idx = find_best_score_idx(scores)
    
    print(sentences[best_matching_score_idx]) # I love machine learning
    print(scores) # [0.9799578870122228, 0.5962847939999439, 0.9622504486493763, 0.8944271909999159]
        
    
sentence_vectors = [
 np.array([1,2,3]),
 np.array([2,1,0]),
 np.array([3,3,3]),
 np.array([0,1,2])
]

sentences = [
 "I love machine learning",
 "Python is great for backend",
 "AI is the future",
 "Football is a great sport"
]

query_vector = np.array([1,2,2])

semantic_search(query_vector, sentence_vectors, sentences)


# -------------------------------------------------

# Q1. Why do we use cosine similarity instead of direct comparison.
# Ans = if use direct comparison they compare by there weight or magnitude not by there direction, on the other hand cosine similarity compare using direction. 

# Q2. time complexity fo semantic search
# Ans = let sentence_vectors is nxm based on this 
#     compute_cosine_similarity is O(m)
#     calculate_scores is O(nxm)
#     find_best_score_idx is O(n) 
    
#     so the time complexity of semantic search is O(nxm) + O(n)

# Q3. How can this become slow with 1 million vectors?
# store normaalized vectors avoid recomputing magnitude 