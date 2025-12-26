sentence = "This is a sample sentence with several words. This sentence is just a sample."

convert_to_list = sentence.lower().replace('.', '').split()
print("List of words:", convert_to_list)
# Output: ['this', 'is', 'a', 'sample', 'sentence', 'with', 'several', 'words', 'this', 'sentence', 'is', 'just', 'a', 'sample']

# Using a dictionary to count occurrences of each word
word_count = {}
for word in convert_to_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Count Dictionary:", word_count)
# Output: {'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'sentence': 2, 'with': 1, 'several': 1, 'words': 1, 'just': 1}
# Displaying the count of each word
for word, count in word_count.items():
    print(f"'{word}': {count}")
# Output:
# 'this': 2
# 'is': 2
# 'a': 2
# 'sample': 2
# 'sentence': 2
# 'with': 1
# 'several': 1
# 'words': 1
# 'just': 1
