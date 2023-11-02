# Example
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Variables
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Apending and Altering
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98
gradebook[-1].remove(98)
gradebook[-1].append("Pass")
full_gradebook = last_semester_gradebook + gradebook

# Prints
print(gradebook)
print(full_gradebook)