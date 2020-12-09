hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
rate = float(rate)

if h <= 40:
    pay = h * rate # user Regular Pay 

elif h > 40:
    otp = (h - 40.0) * (rate * 1.50) # Calculating Overtime of user
    otp = float(otp)
    pay = float(40 * rate + otp) # Calculating The total amount to be paid after overtime
    
print(pay)