#Assignment 11
#Take a string from the user and check contains atleast one digit or no

user_string = raw_input("Enter String:")
count = False
for char in user_string:
    if char.isdigit():
        count = True
if count == True:
    print "\nContains Digit"
else:
    print "\nContains No Digit"
