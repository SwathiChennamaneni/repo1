#5. take a string from the user and check contains only digits or not

user_string = raw_input("Enter String:")
for i in user_string:
    if not i.isdigit():
        flag = 0
    else:
        flag = 1
if flag == 1:
    print "String contains only digits"
else:
    print "Not a Digit only string"
