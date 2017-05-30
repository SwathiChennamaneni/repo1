#9. take a string from the user and check contains only  small letters or not

import re
# Considering the scenario for only small letters without digits
user_string = raw_input("Enter String:")
print "Without Regular Expressions"
for i in user_string:
    if not i.islower():
        flag = 0
        break
else:
    flag = 1
if flag == 1:
    print "\nString contains only Small letters"
else:
    print "\nNot a Small Only String"


user_string1= raw_input("Enter String:")
res = re.match('[a-z].', user_string)
if res:
    print "\nContains only Small letters"
else:
    print "\nNot a Small letter Only String"
