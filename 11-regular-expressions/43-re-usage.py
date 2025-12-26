import re

# EXAMPLE OF ^ USAGE:
# ^ Matches the start of the line.
lines = ['From here to there', 'Hello From there', 'From: someone']
for line in lines:
    if re.search('^From', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: From here to there
# Matched line: From : someone
# In this example, only the line that starts with 'From' is matched.


# $ Matches the end of the line.
lines = ['This is the end', 'This is not the end.', 'End of line$']
for line in lines:
    if re.search('end$', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: This is the end
# In this example, only the line that ends with 'end' is matched.


# . Matches any character that has exactly one character in that position.
lines = ['cat', 'c t', 'caat', 'and', 'act']
for line in lines:
    if re.search('c.t', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat
# Matched line: c t
# In this example, all lines with 'c' followed by any character and then 't' are matched.

# \s Matches a whitespace character.
lines = ['Hello World', 'HelloWorld', 'Hello\tWorld']
for line in lines:
    if re.search('Hello\sWorld', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: Hello World
# Matched line: Hello	World
# In this example, lines with 'Hello' followed by a whitespace character and then 'World' are matched.

# \S Matches a non-whitespace character (opposite of \s).
lines = ['HelloWorld', 'Hello World', 'Hello\tWorld']
for line in lines:
    if re.search('Hello\SWorld', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: HelloWorld
# In this example, only the line with 'Hello' followed by a non-whitespace character and then 'World' is matched.

# * Matches zero or more occurrences of the preceding character.
lines = ['ab', 'aab', 'aaab', 'b', 'ac']
for line in lines:
    if re.search('a*b', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: ab
# Matched line: aab
# Matched line: aaab
# In this example, lines with zero or more 'a's followed by 'b' are matched.


# *? Applies to the immediately preceding character and indicates to match zero or
# more of the preceding character(s) in “non-greedy mode”.
lines = ['aaab', 'aab', 'ab', 'b']
for line in lines:
    match = re.search('a*?b', line)
    if match:
        print(f'Matched line: {line}, Match: {match.group()}')
# OUTPUT:
# Matched line: aaab, Match: b
# Matched line: aab, Match: b
# Matched line: ab, Match: b
# In this example, the non-greedy match finds the shortest sequence of 'a's
# followed by 'b', which is just 'b' in each case.

# + Applies to the immediately preceding character and indicates to match one
# or more of the preceding character(s).
lines = ['ab', 'aab', 'aaab', 'b', 'ac']
for line in lines:
    if re.search('a+b', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: ab
# Matched line: aab
# Matched line: aaab
# In this example, lines with one or more 'a's followed by 'b' are matched.

# +? Applies to the immediately preceding character and indicates to match one
# or more of the preceding character(s) in “non-greedy mode”.
lines = ['aaab', 'aab', 'ab', 'b']
for line in lines:
    match = re.search('a+?b', line)
    if match:
        print(f'Matched line: {line}, Match: {match.group()}')
# OUTPUT:
# Matched line: aaab, Match: ab
# Matched line: aab, Match: ab
# In this example, the non-greedy match finds the shortest sequence of 'a's
# followed by 'b', which is 'ab' in each case.

# [aeiou] Matches a single character as long as that character is in the specified set.
# In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
lines = ['cat', 'cot', 'cnt', 'cmt', 'cit', 'cxt']
for line in lines:
    if re.search('c[aeiou]t', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat
# Matched line: cot
# Matched line: cit
# In this example, lines with 'c' followed by a vowel and then 't'

# [a-z0-9] You can specify ranges of characters using the minus sign. This example
# is a single character that must be a lowercase letter or a digit.
lines = ['cat1', 'cat!', 'catA', 'cat9', 'catz']
for line in lines:
    if re.search('cat[a-z0-9]', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat1
# Matched line: cat9
# Matched line: catz
# In this example, lines with 'cat' followed by a lowercase letter or digit are matched.

# ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic.
# This example matches a single character that is anything other than an uppercase
# or lowercase letter.
lines = ['cat!', 'cat1', 'catA', 'cat@', 'catz']
for line in lines:
    if re.search('cat[^A-Za-z]', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat!
# Matched line: cat1
# Matched line: cat@
# In this example, lines with 'cat' followed by a non-letter character are matched.

# \b Matches the empty string, but only at the start or end of a word.
lines = ['cat', 'concatenate', 'dog cat', 'catalog']
for line in lines:
    if re.search(r'\bcat\b', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat
# Matched line: dog cat
# In this example, only lines where 'cat' appears as a whole word are matched.

# \B Matches the empty string, but not at the start or end of a word.(opposite of \b)
lines = ['cat', 'concatenate', 'dog cat', 'catalog']
for line in lines:
    if re.search(r'\Bcat\B', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: concatenate
# Matched line: catalog
# In this example, only lines where 'cat' appears as part of another word are matched.

# \d Matches any decimal digit; this is equivalent to the set [0-9].
lines = ['cat1', 'cat!', 'catA', 'cat9', 'catz']
for line in lines:
    if re.search(r'cat\d', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat1
# Matched line: cat9
# In this example, lines with 'cat' followed by a digit are matched.

# \D Matches any non-decimal digit; this is equivalent to the set [^0-9]. (opposite of \d)
lines = ['cat1', 'cat!', 'catA', 'cat9', 'catz']
for line in lines:
    if re.search(r'cat\D', line):
        print(f'Matched line: {line}')
# OUTPUT:
# Matched line: cat!
# Matched line: catA
# Matched line: catz
