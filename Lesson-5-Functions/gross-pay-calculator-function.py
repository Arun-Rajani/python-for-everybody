def computepay(hours, rate):
    if hours>40:
        gross_pay = (hours-40) * 1.5 * rate + 40 * rate
    else:
        gross_pay = rate * hours
    return gross_pay
try:
    hours = float(input("Enter hours:"))
    rate = float(input("Enter Rate:"))
    gross_pay = computepay(hours,rate)
    print("Pay",gross_pay)
except:
    print("Enter Numerical Data")