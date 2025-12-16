# This program counts the occurrences of each word in a given line
counts = dict()
line = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"
words = line.split()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
# Output: the 7
# since 'the' is the most frequent word occurring 5 times in the line
