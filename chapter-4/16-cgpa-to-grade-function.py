def cgpa_to_grade(cgpa):
    if cgpa >= 9.0:
        return 'A'
    elif cgpa >= 8.0:
        return 'B'
    elif cgpa >= 7.0:
        return 'C'
    elif cgpa >= 6.0:
        return 'D'
    else:
        return 'F'


# Example usage
grade = cgpa_to_grade(9.2)
print(grade)  # Output : A
grade = cgpa_to_grade(8.5)
print(grade)  # Output : B
grade = cgpa_to_grade(7.3)
print(grade)  # Output : C
