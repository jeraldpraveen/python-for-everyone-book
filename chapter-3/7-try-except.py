# This program asks for the user's name and age, then prints a greeting.
name = input('What is your name?\n')
print('Hello ', name)
age = input('How old are you?\n')
try:
    age = int(age)  # Convert age to an integer
    print(name, ' is ', age, ' years old.')
except ValueError:
    print("Entered age is invalid. Please enter a number.")

# If the user inputs "Jerald" and "25", the output will be: Hello  Jerald
# Jerald  is  25  years old.
# If the user inputs "Jerald" and "twenty five", the output will be: Hello  Jerald
# Entered age is invalid. Please enter a number.
