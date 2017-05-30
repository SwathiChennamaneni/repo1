#Assignment 23  -- Check negative conditions
#Write a program to findout big of two numbers

a = raw_input("Enter First:")
b = raw_input("Enter Second:")
if b.isdigit() and b.isdigit():
    if a>b:
        print "{0} is greater than {1}".format(a,b)
    else:
        print "{0} is greater than {1}".format(b,a)
else:
    print "Enter Digit"
