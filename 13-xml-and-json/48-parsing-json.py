import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
# The program produces the following output:
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7
# This program uses the json module to parse a JSON document stored in a
# string variable. It counts the number of objects in the JSON array and
# iterates through each object to extract and print the name, id, and the
# value of the "x" attribute.
