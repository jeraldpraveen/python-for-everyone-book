stuff = 'Hello Jerald'
# Python has a function called dir which lists the methods available for an object.
print(dir(stuff))
# dir(stuff) returns a list of methods available for an object.
# [capitalize, casefold, center, count, encode, 
# endswith , expandtabs, find, format, format_map, 
# index , isalnum, isalpha, isdecimal, isdigit, 
# isidentifier , islower, isnumeric, isprintable, 
# isspace , istitle, isupper, join, ljust, lower, 
# lstrip , maketrans, partition, replace, rfind, 
# rindex , rjust, rpartition, rsplit, rstrip, 
# split , splitlines, startswith, strip, swapcase, 
# title , translate, upper, zfill]

print(stuff.upper())
# Output : 'HELLO JERALD'