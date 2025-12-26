# Search for lines that contain 'From'
import re
hand = 'From what Is down\nFrom-Jer what Is up\nFrom me to you\nHello From here\n'.splitlines()
for line in hand:
    line = line.rstrip()
    if re.search('From-Jer', line):
        print(line)
# This will print only the line that contains 'From-Jer'
# Output: From-Jer what Is up
# because the other lines do not match the exact pattern 'From-Jer'
