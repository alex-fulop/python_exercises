hours = input("Enter your hours: ")
rate = input("Enter your rate: ")
hours = float(hours)
rate = float(rate)

if hours > 40:
    extra = hours - 40
    pay = hours * rate
    extraPay = extra * (rate * .5)
    print("Pay: ", pay + extraPay)
else:
    pay = hours * rate
    print("Pay: ", pay)