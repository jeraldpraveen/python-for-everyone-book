d = {'a': 10, 'b': 20, 'c': 30}
t = list(d.items())
print(t)
# Output: [('a', 10), ('b', 20), ('c', 30)]
t[0] = ('z', 99)
print(t)
# Output: [('z', 99), ('b', 20), ('c', 30)]

# Converting dictionary items to a tuple
t_tuple = tuple(d.items())
print(t_tuple)
# Output: (('a', 10), ('b', 20), ('c', 30))

# This will raise a TypeError because tuples are immutable when uncommented
# t_tuple[0] = ('z', 99)
