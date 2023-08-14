# Can you create a program to check whether a number is positive or negative or 0?

# To create this program, create a variable named number and assign a float value to it based on the user input. Then using a if statement, check if the number variable is positive or negative or 0.

# If number is positive, print "The number is positive"
# If number is 0, print "The number is 0"
# If number is negative, print "The number is negative"


number = float(input("enter a number: "))

if (number >= 1):
    print("the number is positive")
elif number <= -1:
    print("the number is negative")
else:
    print ("the number is zero")
