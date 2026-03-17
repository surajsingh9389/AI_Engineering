# Embeddings & Vectors: Computers convert words into long lists of numbers (vectors). [0.12, -0.88, ...] is just a NumPy array.

# Vector Databases: These are like "search engines for numbers." They use NumPy-style math to find which lists of numbers are "close" to each other in meaning.

# Similarity Search: If you ask a question, the AI finds the "closest" answer by calculating the distance between two NumPy arrays.

# Deep Learning & Transformers: Models like GPT-4 are essentially massive "math machines." They perform billions of multiplications on grids of numbers (matrices). NumPy is built to do this math incredibly fast.

# Python list
# a = [1,2,3]
# print(a*3)

# print(a*b)

# ---------------------------------------

# numpy array 
# import numpy as np

# a = np.array([2, 4, 6])

# a = a*2  # vectorized operations
# print(a+3)
 
#  Lesson Task 
 
# 1. 
# numpy array 
# import numpy as np

# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])

# addition = a+b
# subtraction = a-b
# multiplication = a*b

# print(addition)
# print(subtraction)
# print(multiplication)
# print(np.dot(a, b))

# 2.
# mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(mat.shape)

# for i in range(len(mat)):
#     print(mat[i])

# for i in range(len(mat[0])):
#     print(mat[:, i])


# ----------------------------------------------------------------
# Step-by-Step Creating normalize vector

# Normalization 
# In AI, Normalization is the process of taking a vector of any size and "shrinking" or "stretching" it so its total mathematical length (magnitude) is exactly 1.0.


# Normalize Vector (Unit Vector)
# To "normalize a vector" means to transform it into a unit vector. It involves dividing each component of the vector by its total length (magnitude).

import numpy as np

# # 1. Create your raw vector (any size)
# v = np.array([3, 4])

# # 2. Calculate the "Magnitude" (The total length)
# magnitude = np.linalg.norm(v) # This vector has a length of 5 (3² + 4² = 25, √25 = 5)

# print(f"Original Length: {magnitude}") # Output: 5.0

# # 3. Divide the vector by its own magnitude
# normalized_v = v / magnitude # Normalized vector

# print(f"Normalized Vector: {normalized_v}") # Output: [0.6, 0.8]


# ----------------------------------------------------------------------------

print(np.ones((2, 3)))
