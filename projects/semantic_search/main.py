import numpy as np

def compute_cosine_similarity(a, b):
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    dot_product = np.dot(a, b)
    
    return dot_product/(magnitude_a*magnitude_b)      
    
 
def calculate_scores(query_vector, sentence_vectors):
    scores = []
    for vector in sentence_vectors:
        current_vector_cs = compute_cosine_similarity(query_vector, vector)
        
        scores.append(current_vector_cs)
        
    return scores    
    

# def get_top_matches(scores):
#     new_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    
#     return new_scores

def get_top_k(scores, k):
    if k == 0 or k > len(scores): 
        return []
    
    new_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    
    return new_scores[:k]
        
    

def semantic_search(query_vector, sentence_vectors, sentences, k):
    scores =  calculate_scores(query_vector, sentence_vectors)

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

k = int(input("How many top matches you want?: "))

top_result  = semantic_search(query_vector, sentence_vectors, sentences, k)
print(top_result)

