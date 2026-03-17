# Cosine similarity is a metric used to measure the similarity between two non-zero vectors by calculating the cosine of the angle between them.
# Mathematically, it is defined as the dot product of the two vectors divided by the product of their magnitudes (lengths).

# The Formula = 

# note - if vector are not normalized
# cosine Similarity = {A.B} /{|A||B|}

# and if vector are normalized = np.dot(a, b)

# 0 = means not related (orthogonal)
# 1 = means same direction
# -1 = means opposite direction

import numpy as np

# Task 1.
def cosine_similarity(a, b):
    # mehtod 1.
    dot_prod = np.dot(a, b)
    
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    
    # empty text → zero vector → crash (division by zero)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    return dot_prod/(magnitude_a*magnitude_b)
    
    # # method 2.
    # magnitude_a = np.linalg.norm(a)
    # magnitude_b = np.linalg.norm(b)
    
    # normalize_vector_a = a/magnitude_a
    # normalize_vector_b = b/magnitude_b
    
    # return np.dot(normalize_vector_a, normalize_vector_b)
    
# ----------------------------------------------------

# Task 2.
# a = np.array([1, 2, 3])
# b = np.array([1, 2, 3])

# print(cosine_similarity(a, b)) # 1.0

# a = np.array([1, 0])
# b = np.array([0, 1])

# print(cosine_similarity(a, b)) # 0.0

# a = np.array([1, 0])
# b = np.array([1, 0])

# print(cosine_similarity(a, b)) # 1.0

# --------------------------------------------------

# Task 3. 
# Euclidean Distance cares about distance (the gap between two points).
# Cosine Similarity cares about direction (the angle between two arrows).
# The AI rule of thumb:
# If you want to know if two things have the same meaning (like two sentences), use Cosine. If you want to know if two things have the same values (like height and weight), use Euclidean.



# i just want to know when we learn remaining concept of numpy for ai Engineering, also you explain the concept really short which sometime did not undertand, explain concept clearly with examples.