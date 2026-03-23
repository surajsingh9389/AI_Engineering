import numpy as np
import heapq

# def compute_similarity(a, b):
#     # magnitude_a = np.linalg.norm(a)
#     # magnitude_b = np.linalg.norm(b)
    
#     # if magnitude_a == 0 or magnitude_b == 0:
#     #     return 0
    
#     # dot_product = np.dot(a, b)
    
#     # return dot_product/(magnitude_a*magnitude_b)   
    
#     return np.dot(a, b)   
    
 
# def calculate_scores(query_vector, sentence_vectors):
#     scores = []
#     for vector in sentence_vectors:
#         current_vector_cs = compute_similarity(query_vector, vector)
        
#         scores.append(current_vector_cs)
        
#     return scores    
    

# def get_top_matches(scores):
#     new_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    
#     return new_scores

def get_top_k(scores, k):
    if k == 0 or k > len(scores): 
        return []
    
    # new_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    
    new_scores = heapq.nlargest(k, enumerate(scores), key=lambda x: x[1])
    
    return new_scores
        
def get_normalize_vector(vector):
    vector_magnitude = np.linalg.norm(vector)
    
    if vector_magnitude == 0:
        return vector
    
    return vector/vector_magnitude 
   

def semantic_search(normalize_query_vector, normalize_sentence_vectors, sentences, k):
    
    # scores =  calculate_scores(normalize_query_vector,normalize_sentence_vectors)
    
    scores = [np.dot(normalize_query_vector, v) for v in normalize_sentence_vectors]

    # top_matches = get_top_matches(scores)
    
    # top1 = top_matches[0]
    # top2 = top_matches[1]
    
    # for best sentence and best sentence score 
    # print(sentences[top1[0]])
    # print(scores) 
    # print(scores[top1[0]])
    
    top_matches = get_top_k(scores, k)
    top_matches_with_score = []
    
    for pair in top_matches:
        idx = pair[0]
        score = pair[1]
        
        top_matches_with_score.append((sentences[idx], score))
    
    return top_matches_with_score

    # return [
    #     (sentences[top1[0]], top1[1]),
    #     (sentences[top2[0]], top2[1]),
    # ]

        
    
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

normalize_sentence_vectors = [get_normalize_vector(v) for v in sentence_vectors]
    
normalize_query_vector = get_normalize_vector(query_vector)

k = int(input("How many top matches you want?: "))

top_result  = semantic_search(normalize_query_vector, normalize_sentence_vectors, sentences, k)

print(top_result)








