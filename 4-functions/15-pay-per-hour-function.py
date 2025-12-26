def pay_per_hour(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)


# Example usage
total_pay = pay_per_hour(45, 10)
print(total_pay)  # Output : 475.0
total_pay = pay_per_hour(38, 10)
print(total_pay)  # Output : 380
