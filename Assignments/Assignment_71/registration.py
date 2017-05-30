from db_operations import DB
import sqlite3

# Creates Table only if doesnot exist
DB().create_table("Name","Age","Gender","Mobile")
    
class Model(object):
    def create(self):
        print "To Register, Enter Below Details"
        name = raw_input("Enter Name:")
        age = input("Enter Age:")
        gender = raw_input("Enter Gender:")
        mobile = input("Enter Mobile Number:")
        DB().insert_values(name,age,gender,mobile)

class Person(Model):
    # Overrided create() of Parent Class
    def create(self):
        # Calling Parent Class create()
        super(Person,self).create()
        print "You are Registered Successfully"

# Calling Child Class create()
p=Person()
p.create()
