#Assignment 21
#Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger

age = raw_input("Please enter the age:")
if not age.isalpha():
    age = int(age)
    if age in range(0,1):
        print "Given age falls under Baby age group"
    elif age in range(1,3):
        print "Given age falls under Toddler age group"
    elif age in range(3,13):
        print "Given age falls under Childage group"
    elif age in range(13,19):
        print "Given age falls under Teenage group"
    elif age in range(19,66):
        print "Given age falls under Adult age group"
    elif age > 65:
        print "Given age falls under Oldcodger group"
    else:
        print "Please enter positive numbers for age"
else:
    print "Please enter positive numbers for age"
