#Assignment 20
#Take two numbers from the user a,b check whether a is divisible by b or not

a = input("Enter a number:")
b = input("Enter a number:")
if a%b == 0:
    print "{0} is divisible by {1}".format(a,b)
else:
    print "{0} is not divisible by {1}".format(a,b)
