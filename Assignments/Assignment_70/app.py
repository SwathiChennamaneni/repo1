from db_operations import DB
import sys

def Details():
    db = DB()
    # Creates Table if doesnot exist already 
    db.create_table("registration","Name","Age","Gender","Mobile")
    
    # Considering Registration Example, Taking Inputs from User
    print ("Options \n1.Register\n2.Update\n3.Delete\n4.Exit\n")
    select = raw_input("Select Option:")
    if select == '1':
        name = raw_input("Enter Name:")
        age = input("Enter Age:")
        gender = raw_input("Enter Gender:")
        mobile = input("Enter Mobile Number:")
        # Inserting Values in to database
        db.insert_values('registration',name,age,gender,mobile)
        cont = raw_input("Do you want to continue[y/n]")
        if cont =="y":
            Details()
    elif select == '2':
        rid = raw_input("Enter Your ID:")
        mobile = raw_input("Enter Your Mobile Number:")
        # Updating Values in Database
        db.update_values('registration',rid,mobile)
        cont = raw_input("\nDo you want to continue[y/n]\n")
        if cont =="y":
            Details()
    elif select == '3':
        rid = raw_input("Enter Your ID:")
        # Deleting Values from Databse
        db.delete_values('registration',2)
        print "Deleted Record\n"
        cont = raw_input("Do you want to continue[y/n]")
        
        if cont =="y":
            Details()
    elif select =='4':
        sys.exit()
    else:
        print "Enter Valid Option"
        Details()

Details()
