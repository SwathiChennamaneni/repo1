#Assignment 15
#Take a string from the user and check contains atleast one small letter or not?

user_string = raw_input("Enter a String:")
count = False
for char in user_string:
    if char.islower():
        count = True

if count == True:
    print "\nContains Small Letter"
else:
    print "\nContains No Small Letters"
