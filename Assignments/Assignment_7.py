#7. take a string from the user and check contains only  special chars or not

import re
#Written by considering all other than alphabets,digits as special characters

user_string = raw_input("Enter String:")
res = re.match("^[a-zA-Z0-9]?", user_string)
if res:
    print "Contains Only special Characters"
else:
    print "Not a Special Character Only String"
