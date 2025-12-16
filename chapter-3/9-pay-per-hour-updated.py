# This program calculates total pay including overtime for hours worked over 40.
# Overtime is paid at 1.5 times the regular hourly rate.
hourly_rate = float(input("Enter your hourly pay rate: "))
hours_worked = float(input("Enter number of hours worked: "))
total_pay = float(hourly_rate) * float(hours_worked)
if hours_worked > 40:
    overtime_hours = float(hours_worked) - 40
    regular_pay = 40 * float(hourly_rate)
    overtime_pay = overtime_hours * float(hourly_rate) * 1.5
    total_pay = regular_pay + overtime_pay
    print("Your total pay is: ", total_pay)
else:
    print("Your total pay is: ", total_pay)

# Case with overtime
# Output : Your total pay is:  712.5
# if hourly_rate = 15 and hours_worked = 45
# Case without overtime
# Output : Your total pay is:  375.0
# if hourly_rate = 15 and hours_worked = 25
