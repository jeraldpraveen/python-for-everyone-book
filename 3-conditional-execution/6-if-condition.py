# This program checks if the user input is empty (null) or not.
user_input = input('What is your name?\n')

if not user_input:   # empty string evaluates to False
    print("Input is empty (null).")
else:
    print("You entered:", user_input)

# If the user inputs "Jerald", the output will be: You entered: Jerald
# If the user just presses Enter without typing anything, the output will be: Input is empty (null).
