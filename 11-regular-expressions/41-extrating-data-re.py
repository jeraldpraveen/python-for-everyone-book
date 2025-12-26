import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# Find all email addresses in the string
# An email address is defined here as a sequence of non-whitespace characters
# followed by '@', followed by another sequence of non-whitespace characters
lst = re.findall('\S+@\S+', s)
print(lst)
