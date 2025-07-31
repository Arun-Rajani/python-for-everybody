hrs = input("Enter hours:")
rate = input("Enter Rate:")
hours = float(hrs)
if hours>40:
    normal_pay = 40 * float(rate)
    overtime_hrs = hours - 40
    overtime_pay = overtime_hrs * 1.5 * float(rate)
    gross_pay = overtime_pay + normal_pay
    print(gross_pay)
else:
    normal_pay = float(rate) * hours
    print(normal_pay)