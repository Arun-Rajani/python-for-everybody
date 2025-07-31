try:
    hrs = input("Enter hours:")
    rate = input("Enter Rate:")
    pay = float(hrs)*float(rate)
    print("Pay:",pay)
except:
    print("Please enter numerical values")