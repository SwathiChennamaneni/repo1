from Employee_info import DB

#db= DB()
#db.create_table("EMPLOYEE","ID","Name","Age","Address","Salary","Height","Weight")

def Input_Emp():
    eid = raw_input("Enter Your Employee ID:")
    ename = raw_input("Enter Your Name:")
    eage = raw_input("Enter Your Age:")
    eaddress = raw_input("Enter Your Address:")
    esal = raw_input("Enter Your Salary:")
    eheight = raw_input("Enter Your Height in cms:")
    eweight = raw_input("Enter Your Weight:")
    DB().insert_values(eid,ename,eage,eaddress,esal,eheight,eweight)
    
    cont = raw_input("Do you want to Continue[Y/N]:")
    if cont == "Y":
        Input_Emp()
    else:
        print "Thank You .."



def Emp_Info():
    eid = raw_input("Enter Your ID:")
    DB().Get_Emp_Info(eid)
    

def Emp_Avg_Sal():
    DB().Get_Sal()

def EMP_High_Sal():
    DB().High_Sal()

def EMP_BMI():
    DB().BMI_Val()

def Org_BMI():
    DB().Overall_BMI_Val()

if __name__=='__main__':
    #db.create_table("EMPLOYEE","ID","Name","Age","Address","Salary","Height","Weight")
    print "\n ** Input **"
    Input_Emp()
    print "\n ** Get Employee Info.. **"
    Emp_Info()
    print "\n ** Average Salary of Employees **"
    Emp_Avg_Sal()
    print "\n ** Highest Salary of Employee **"
    EMP_High_Sal()
    print "\n ** BMI of all the Employees **"
    EMP_BMI()
    print "\n ** Overall Org BMI **"
    Org_BMI()
