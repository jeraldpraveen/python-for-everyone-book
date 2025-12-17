# Example of a for loop that iterates over a list of friends
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Example of a for loop that counts down from 5 to 1
total = 0
for i in [5, 4, 3, 2, 1]:
    total = total + i
print('Total:', total)
# Output : Total: 15

largest = None
print('Before:', largest)
for value in [3, 41, 12, 9, 74, 15]:
    if largest is None or value > largest:
        largest = value
    print('Loop:', value, largest)
print('Largest:', largest)
# Output :
# Before: None
# Loop: 3 3
# Loop: 41 41
# Loop: 12 41
# Loop: 9 41
# Loop: 74 74
# Loop: 15 74
# Output : Largest: 74
# Example of using range() in a for loop to count from 0 to 4
for i in range(5):
    print(i)
# Output : 0 to 4

# Example of using range() in a for loop to count from 5 to 9
for i in range(5, 10):
    print(i)
# Output : 5 to 9

# Example of using range() in a for loop to count from 0 to 10 in steps of 2
for i in range(0, 11, 2):
    print(i)
# Output : 0, 2, 4, 6, 8, 10
# Example of summing numbers using range() in a for loop
total = 0
for i in range(1, 6):
    total = total + i
print('Total:', total)
# Output : Total: 15
# Example of finding the largest number using range() in a for loop
largest = None
for i in range(1, 10):
    if largest is None or i > largest:
        largest = i
print('Largest:', largest)
# Output : Largest: 9
# Example of iterating over a string using a for loop
for char in 'banana':
    print(char)
# Output : b a n a n a
# Example of iterating over a tuple using a for loop
tup = (3, 1, 4, 1, 5, 9)
for item in tup:
    print(item)
# Output : 3 1 4 1 5 9
# Example of iterating over a dictionary using a for loop
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
# Output : a 1 \n b 2 \n c 3
for key, value in d.items():
    print(key, value)
# Output : a 1 \n b 2 \n c 3
for value in d.values():
    print(value)
# Output : 1 \n 2 \n 3
# Example of using enumerate() in a for loop to get index and value
friends = ['Joseph', 'Glenn', 'Sally']
for index, friend in enumerate(friends):
    print(index, friend)
# Output : 0 Joseph \n 1 Glenn \n 2 Sally
# Example of nested for loops to print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()

# Output :
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20
# 5	10	15	20	25
# Example of using break in a for loop
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# Output : 1 2 3 4
# Example of using continue in a for loop
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
# Output : 1 3 5 7 9
# Example of using else in a for loop
for i in range(1, 6):
    print(i)
else:
    print('Loop completed successfully!')
# Output : 1 2 3 4 5 \n Loop completed successfully!
# Example of using pass in a for loop
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
# Output : 1 2 3 4 5
# Example of using zip() in a for loop to iterate over two lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
# Output : Alice 25 \n Bob 30 \n Charlie 35
# Example of using reversed() in a for loop to iterate over a list in reverse order
for i in reversed(range(1, 6)):
    print(i)
# Output : 5 4 3 2 1
# Example of using sorted() in a for loop to iterate over a list in sorted order
unsorted_list = [5, 2, 9, 1, 5, 6]
for i in sorted(unsorted_list):
    print(i)
# Output : 1 2 5 5 6 9
