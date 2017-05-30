# Assignment 12
#Take a string from the user and check contains atleast one alphabets or not

user_string = raw_input("Enter a String:")
ccount = False
for char in user_string:
    if char.isalpha():
        count = True

if count == True:
    print "\nContains Alphabet"
else:
    print "\nContains No Alphabet"
