list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# List concatenation
combined_list = list1 + list2
print("Combined List:", combined_list)  # Output: [1, 2, 3, 'a', 'b', 'c']
# List repetition
repeated_list = list1 * 3
print("Repeated List:", repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# List Slicing
sliced_list = combined_list[2:5]
print("Sliced List:", sliced_list)  # Output: [3, 'a', 'b']
# Modifying list elements
combined_list[0] = 10
print("Modified Combined List:", combined_list)
# Output: [10, 2, 3, 'a', 'b', 'c']
