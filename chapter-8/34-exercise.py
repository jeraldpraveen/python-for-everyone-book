get_input = []


val = int(input("Enter a number: "))
get_input.append(val)
while val != 'done':
    val = input("Enter a number: ")
    if (val == 'done'):
        break
    get_input.append(int(val))

print("You entered:", get_input)

print("Maximum value:", max(get_input))
print("Minimum value:", min(get_input))
