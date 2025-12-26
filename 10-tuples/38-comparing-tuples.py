# Tuples can be compared using comparison operators like <, <=, >, >=, ==, and !=.
check = (1, 2, 3) < (1, 2, 4)
print("Is (1, 2, 3) less than (1, 2, 4)", check)
# Output: Is (1, 2, 3) less than (1, 2, 4) True
# Comparing tuples in Python is done lexicographically, meaning that the first elements are compared first.

check = (1, 2, 3) == (1, 2, 3)
print("Is (1, 2, 3) equal to (1, 2, 3)", check)
# Output: Is (1, 2, 3) equal to (1, 2, 3) True
