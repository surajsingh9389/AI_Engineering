# Embedding: A list of numbers that represents the meaning of an object, so a computer can find other objects with a similar meaning by comparing those numbers.

# age = 12
# if(age > 10): 
#     print(age)

# age = input("what is your age?")

# age = int(age)

# print("age is ", str(age))

# year = input("Enter a year: ")
# year = int(year)

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(str(year) + " is a leap year!")
# else:
#     print(str(year) + " is not a leap year.")



# # Looping through a string (each character)
# for letter in "Python":
#     print("Letter:", letter)

# # Looping through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print("I like", fruit)

# # Using range() - generates a sequence of numbers
# for i in range(5):        # 0, 1, 2, 3, 4
#     print("Number:", i)

# for i in range(1, 6):      # 1, 2, 3, 4, 5
#     print("Count:", i)

# for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (start, stop, step)
#     print("Even:", i)



num = input("Enter a number: ")
num = int(num)

for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = ", num*i)