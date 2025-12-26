import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
# The program produces the following output:
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7
# This program parses an XML document containing user information. It counts
# the number of user elements and iterates through each user to extract and
# print their name, id, and the value of the "x" attribute.
