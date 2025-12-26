def count_letters(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count

print(count_letters("hello", "l"))
# Output : 2

print(count_letters("banana", "a"))
# Output : 3