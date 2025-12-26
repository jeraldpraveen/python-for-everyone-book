import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)  # Output: ['$10.00']
# In the pattern '\$[0-9.]+' the dollar sign is escaped with a backslash
# so that it is treated as a literal character rather than a special regex symbol.
# The pattern matches a dollar sign followed by one or more digits or periods.
# This is useful when you want to search for actual dollar amounts in text.
# Without the escape, the dollar sign would have a special meaning in regex,
# typically indicating the end of a string, which is not what we want here.
# Therefore, escaping special characters is crucial when you want to match them literally in your text.

x = 'The price is 5 dollars.'
y = re.findall('\$[0-9.]+', x)
print(y)  # Output: []
# In this case, there is no dollar sign in the string,
# so the pattern does not match anything and returns an empty list.
