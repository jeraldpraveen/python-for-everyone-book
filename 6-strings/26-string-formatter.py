# The format operator, % allows us to construct strings, replacing parts of the strings with the data stored in variables.
camels = 42
statement1 = 'I have spotted %d camels.' % camels
print(statement1)
# Output : I have spotted 42 camels.

statement2 = 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
print(statement2)
# Output : In 3 years I have spotted 0.1 camels.