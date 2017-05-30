# Assignment 13 -- CONFIRM what is the difference between 12 and 13
#Take a string from the user and check contains atleast one chars or not

user_string = raw_input("Enter a String:")
count = False
for char in user_string:
    if not char.isalnum():
        count = True

if count == True:
    print "\nContains Special Character"
else:
    print "\nContains No Special Characters"
