# A tuple is a sequence of immutable Python objects.
# Tuples are similar to lists, but the difference is that tuples cannot be changed unlike lists.
# Tuples are immutable, so we cannot change their elements
new_tuple = (1, 2, 3)
print("Attempting to change an element will raise an error.")
# Uncommenting the following line will raise a TypeError
# my_tuple[0] = 10

# Tuples are defined by enclosing the elements in parentheses ().
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Output: First element: 1
print("Last element:", my_tuple[-1])  # Output: Last element: 5


# However, we can concatenate tuples to create a new tuple
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)
# Output: Concatenated tuple: (1, 2, 3, 4, 5, 6, 7, 8)

# We can also unpack tuples into variables
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)  # Output: Unpacked values: 1 2 3 4 5
# Tuples can contain mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
# Output: Mixed tuple: (1, 'Hello', 3.14, True)
print("Mixed tuple:", mixed_tuple)
# Tuples can be nested
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested tuple:", nested_tuple)
# Output: Nested tuple: (1, (2, 3), (4, 5, 6))
