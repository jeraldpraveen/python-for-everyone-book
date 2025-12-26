test_word = 'praveendevadas.arokkiajerald@microchip.com is my mail id'

# Get domain name from the mail id
at_position = test_word.find('@')
print(at_position)
empty_space_after_at = test_word.find(' ', at_position)
print(empty_space_after_at)
data = test_word[at_position+1:empty_space_after_at]
print(data)

# Use find and string slicing to extract the portion of the string after the colon character and 
# then use the float function to convert the extracted string into a f loating point number.
str = 'X-DSPAM-Confidence:0.8475'
index_of_colon = str.find(':')
value = str[index_of_colon+1:]
print(float(value))


