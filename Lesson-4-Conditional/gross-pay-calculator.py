hours = float(input("Enter hours:"))
rate = float(input("Enter Rate:"))
if hours>40:
    gross_pay = (hours-40) * 1.5 * rate + 40 * rate
else:
    gross_pay = rate * hours
print(gross_pay)