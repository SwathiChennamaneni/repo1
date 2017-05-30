#Assignment 14
#Take a string from the user and check contains atleast one capital letter or no

user_string = raw_input("Enter a String:")
count = False
for char in user_string:
    if char.isupper():
        count = True

if count == True:
    print "\nContains Capital Letter"
else:
    print "\nContains No Capital Letters"
