# Example of using itertools.cycle() in a for loop to create an infinite loop
import itertools
count = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if count >= 6:
        break
    print(item)
    count += 1
# Output : A B C A B C
# Example of using itertools.count() in a for loop to count indefinitely
for i in itertools.count(10, 5):
    if i > 30:
        break
    print(i)
# Output : 10, 15, 20, 25, 30
# Example of using itertools.repeat() in a for loop to repeat an item
for item in itertools.repeat('Hello', 3):
    print(item)
# Output : Hello Hello Hello
# Example of using itertools.chain() to iterate over multiple iterables
for item in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
    print(item)
# Output : 1 2 3 a b c
# Example of using itertools.islice() to slice an iterable
for item in itertools.islice(itertools.count(), 5, 15, 2):
    print(item)
# Output : 5, 7, 9, 11, 13
# Example of using itertools.combinations() to get combinations of items
for combo in itertools.combinations(['A', 'B', 'C', 'D'], 2):
    print(combo)
# Output : ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')
# Example of using itertools.permutations() to get permutations of items
for perm in itertools.permutations(['A', 'B', 'C'], 2):
    print(perm)
# Output : ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')
# Example of using itertools.product() to get the Cartesian product of items
for prod in itertools.product(['A', 'B'], [1, 2]):
    print(prod)
# Output : ('A', 1) ('A', 2) ('B', 1) ('B', 2)
# Example of using itertools.groupby() to group items
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# Output :
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
# C [('C', 5)]
# Example of using itertools.accumulate() to get cumulative sums
for total in itertools.accumulate([1, 2, 3, 4, 5]):
    print(total)
# Output : 1, 3, 6, 10, 15
# Example of using itertools.tee() to create multiple independent iterators
iter1, iter2 = itertools.tee(range(5), 2)
for item in iter1:
    print('Iter1:', item)
for item in iter2:
    print('Iter2:', item)
# Output :
# Iter1: 0
# Iter1: 1
# Iter1: 2
# Iter1: 3
# Iter1: 4
# Iter2: 0
# Iter2: 1
# Iter2: 2
# Iter2: 3
# Iter2: 4
# Example of using itertools.filterfalse() to filter items
for item in itertools.filterfalse(lambda x: x % 2 == 0, range(10)):
    print(item)
# Output : 1, 3, 5, 7, 9
# Example of using itertools.compress() to filter items based on selectors
data = ['A', 'B', 'C', 'D', 'E']
selectors = [1, 0, 1, 0, 1]
for item in itertools.compress(data, selectors):
    print(item)
# Output : A C E
# Example of using itertools.zip_longest() to zip iterables of different lengths
for item in itertools.zip_longest(['A', 'B', 'C'], [1, 2]):
    print(item)
# Output : ('A', 1) ('B', 2) ('C', None)
# Example of using itertools.starmap() to apply a function to items
for result in itertools.starmap(lambda x, y: x + y, [(1, 2), (3, 4), (5, 6)]):
    print(result)
# Output : 3, 7, 11
# Example of using itertools.dropwhile() to drop items while a condition is true
for item in itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 6, 7, 4, 5]):
    print(item)
# Output : 6, 7, 4, 5
# Example of using itertools.takewhile() to take items while a condition is true
for item in itertools.takewhile(lambda x: x < 5, [1, 2, 3, 6, 7, 4, 5]):
    print(item)
# Output : 1, 2, 3
# Example of using itertools.chain.from_iterable() to flatten a list of lists
nested_list = [[1, 2], [3, 4], [5]]
for item in itertools.chain.from_iterable(nested_list):
    print(item)
# Output : 1 2 3 4 5
# Example of using itertools.pairwise() to get consecutive pairs
for a, b in itertools.pairwise([1, 2, 3, 4, 5]):
    print(a, b)
# Output : (1, 2) (2, 3) (3, 4) (4, 5)
# Example of using itertools.repeat() to create an infinite iterator
for item in itertools.islice(itertools.repeat('Python'), 4):
    print(item)
# Output : Python Python Python Python
# Example of using itertools.cycle() with a break condition
for index, item in enumerate(itertools.cycle(['X', 'Y', 'Z'])):
    if index >= 5:
        break
    print(item)
# Output : X Y Z X Y
# Example of using itertools.count() with a condition
for number in itertools.count(1):
    if number > 5:
        break
    print(number)
# Output : 1 2 3 4 5
