# This program converts CGPA to grades.
enter_cgpa = input("Enter your CGPA between 1 to 10: ")
cgpa = float(enter_cgpa)
if cgpa >= 9.0 and cgpa <= 10.0:
    grade = 'A'
elif cgpa >= 8.0 and cgpa < 9.0:
    grade = 'B'
elif cgpa >= 7.0 and cgpa < 8.0:
    grade = 'C'
elif cgpa >= 6.0 and cgpa < 7.0:
    grade = 'D'
elif cgpa >= 5.0 and cgpa < 6.0:
    grade = 'E'
elif cgpa >= 1.0 and cgpa < 5.0:
    grade = 'F'
else:
    grade = 'Invalid CGPA entered'
print("Your grade is: ", grade)

# Example Outputs:
# If CGPA = 9.2, Output: Your grade is:  A
# If CGPA = 7.5, Output: Your grade is:  C
# If CGPA = 4.8, Output: Your grade is:  F
# If CGPA = 11, Output: Your grade is:  Invalid CGPA entered
# If CGPA = -2, Output: Your grade is:  Invalid CGPA entered
