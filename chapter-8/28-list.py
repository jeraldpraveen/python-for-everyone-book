# Example of a list containing different data types
list_example = ['spam', 2.0, 5, [10, 20]]
print(list_example)
print("spam" in list_example)  # Output: True

# Accessing elements in the list
print(list_example[0])      # Output: 'spam'
print(list_example[3])      # Output: [10, 20]
print(list_example[3][1])   # Output: 20

print("List length:", len(list_example))  # Output: List length: 4
# Output: Max value in sublist: 20
print("Max value in sublist:", max(list_example[3]))
# Modifying elements in the list
list_example[1] = 'eggs'
print(list_example)  # Output: ['spam', 'eggs', 5, [10, 20]]

# List concatenation
new_list = list_example + ['bacon', 3.14]
print(new_list)  # Output: ['spam', 'eggs', 5, [10, 20], 'bacon', 3.14]
