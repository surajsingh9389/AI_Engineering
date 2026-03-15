fav = ["GTA", "RED", "AVG", "OP", "DB", "BLEACH"]
# print(fav[0], fav[len(fav)-1])
# fav.append("HXH")
# print(fav)
# fav.insert(2, "SXF")
# print(fav)
# fav.pop()

# print(fav[-3::-2]) 

# ----------------------------------------------------------------------


grade = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88
}

grade["Tom"] = 95
grade["Bob"] = 99

# std_count = len(grade)
# total_grade = 0

# for key, val in grade.items():
#     total_grade+=val

print(grade)

grade_min = min(grade.values())
grade_max = max(grade.values())

print(grade_min, grade_max)

# print(total_grade/std_count)