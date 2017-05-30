#Assignment 10

#Show the below menu to the user until and until user select quit and display corresponding os message
#Menu:
#1. windows
#2. Linux
#3. Mac
#4. quit

while True:
    print "\nSelect one of the below Options\nMenu:\n1. Windows\n2. Linux\n3. Mac\n4. Quit"
    Select = raw_input("Enter Option:")
    if Select == '1':
        print "\nYou have selected Windows O/S"
    elif Select == '2':
        print "\nYou have selected Linus O/S"
    elif Select == '3':
        print "\nYou have selected Mac O/S"
    elif Select == '4':
        print "\nThank you"
        break
