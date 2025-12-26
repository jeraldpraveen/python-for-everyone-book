a = 'banana'
b = 'banana'
# Both refer to the same string object
print(a is b)  # Output: True

a = [1, 2, 3]
b = [1, 2, 3]
# They are different list objects
print(a is b)  # Output: False

c = a
# c refers to the same list object as a
print(a is c)  # Output: True
