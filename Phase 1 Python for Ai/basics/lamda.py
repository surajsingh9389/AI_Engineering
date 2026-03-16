# lambda arguments: expression


# 1. Assigning it to a Variable (Simple Use)

# def double(x):
#     return x * 2

# double = lambda x: x * 2
# print(double(5))


# --------------------------------------------------------------------

#3. Inside "High-Order" Functions 
# nums = [1, 5, 10, 15]
# Keep only numbers greater than 7
# big_nums = list(filter(lambda x: x > 7, nums)) 
# Result: [10, 15]


# -------------------------------------------------------------------------

# 3. C. With Sorting (sort or sorted) 

repos = [{"name": "A", "stars": 50}, {"name": "B", "stars": 10}]

# Sort the list based on the "stars" key
repos.sort(key=lambda repo: repo["stars"])