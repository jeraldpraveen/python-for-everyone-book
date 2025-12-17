def print_twice(message):
    print(message)
    print(message)


print_twice("Hello, World!")
# Output:
# Hello, World!
# Hello, World!

# Argument is evaluated before being passed to the function in following two examples
print_twice("Spam" * 3)
# Output:
# SpamSpamSpam
# SpamSpamSpam

print_twice(42*2)
# Output:
# 84
# 84
