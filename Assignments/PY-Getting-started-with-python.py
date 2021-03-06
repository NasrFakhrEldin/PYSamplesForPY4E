# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.


hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error, Please enter numeric input")
    quit()
    
if hrs > 40:
    pay = 40 * rate
    x = hrs - 40
    rate *= 1.5
    total = pay + (rate * x)
    print(total)
else:
    print(hrs * rate)


# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

def computepay(hrs, rate):

    try:
        hrs = float(hrs)
        rate = float(rate)
    except:
        print("Error, Please enter numeric input")
        quit()

    if hrs > 40:
        pay = 40 * rate
        x = hrs - 40
        rate *= 1.5
        total = pay + (rate * x)
        print("Pay", total)
    else:
        print("Pay", hrs * rate)
        
    return hrs, rate    
p = computepay(float(input("Enter Hours")), float(input("Enter Rate")))