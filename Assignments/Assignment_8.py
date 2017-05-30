#8. take a string from the user and check contains only  capiatl letters or not

import re
user_string = raw_input("Enter String:")
print "Without Regular Expressions"
for i in user_string:
    if not i.isupper():
        flag = 0
        break
else:
    flag = 1
if flag == 1:
    print "\nString contains only Capital letters"
else:
    print "\nNot a Capital Only String"
user_string1 = raw_input("\nEnter String:")
print "With Regular Expressions"
# checking only for chars in string not for digits
res = re.match('[A-Z].', user_string1)
if res:
    print "\nContains only Capital letters"
else:
    print "\nNot a Capital Only String"
