import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text.strip())
# The program produces the following output:
# Name: Chuck
# Attr: yes
# Phone: +1 734 303 4456
# This program uses the xml.etree.ElementTree module to parse a small XML
# document stored in a string variable. It extracts and prints the name, the
# value of the "hide" attribute from the email element, and the phone number,
# demonstrating how to navigate and retrieve data from an XML structure.
