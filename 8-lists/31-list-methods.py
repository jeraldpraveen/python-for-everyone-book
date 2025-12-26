t = ['a', 'b', 'c']
t.append('d')
print("After append:", t)  # Output: ['a', 'b', 'c, 'd']
t = [1, 2, 3]
t.extend([4, 5])
print("After extend:", t)  # Output: [1, 2, 3, 4, 5]
t = [1, 2, 3]
t.insert(1, 'x')
print("After insert:", t)  # Output: [1, 'x', 2, 3]
t = [1, 2, 3, 4, 5]
del t[1]
print("After del:", t)  # Output: [1, 3, 4, 5]
t = [1, 2, 3, 4, 5]
t.remove(3)
print("After remove:", t)  # Output: [1, 2, 4, 5]
t = [1, 2, 3, 4, 5]
popped_element = t.pop()
print("After pop:", t)  # Output: [1, 2, 3, 4]
print("Popped element:", popped_element)  # Output: 5

# Demonstrating various list methods
t = [3, 1, 4, 2]
t.sort()
print("After sort:", t)  # Output: [1, 2, 3, 4]
t = ['banana', 'apple', 'cherry']
t.sort()
print("After sort (strings):", t)  # Output: ['apple', 'banana', 'cherry']
t = [3, 1, 4, 2]
t.reverse()
print("After reverse:", t)  # Output: [2, 4, 1, 3]

nums = [3, 41, 12, 9, 74, 15]
print("Max number:", max(nums))
print("Min number:", min(nums))
print("Sum of numbers:", sum(nums))
print("Average:", sum(nums) / len(nums))
