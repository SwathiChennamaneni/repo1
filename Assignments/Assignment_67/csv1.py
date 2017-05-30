import os
import sys
select = True

while select:
    print "\n***** Menu *****"
    print "1. Get Employee Information\n2. Modify Employee Information\n3. Delete Employee Information\n4. Add Employee Information\n5. Quit"
    select = raw_input("\nSelect:")

    if not os.path.exists("D:\py_programs\Assignments\Assignment_67\emp.csv"):
        columns=['Id','Name','Age','Salary','Status']
        f = open("emp.csv","w")
        rows=[]
        rows.insert(0,",".join(columns)+"\n")
        f.writelines(rows)
        f.close()
        last = 1
    else:
        t_d = open("emp.csv","r").readlines()
        count = len(t_d[1:])
        if count:
            last = int(t_d[count][0]) + 1
        else:
            last = 1

    if select == '4' :
        #ID = last + int(1)
        Name = raw_input("Enter Name:")
        Age=raw_input("Enter Age:")
        Salary = raw_input("Enter Salary:")
        Status = "Active"
        rows=[]
        f = open("emp.csv","a")
        row = "{0},{1},{2},{3},{4}\n".format(last,Name,Age,Salary,Status)
        rows.append(row)
        f.writelines(rows)
        print "Row Updated Successfully And"
        print "Employee Id is:",last
        f.close()
        
    elif select == '2':
        ID = raw_input("Enter ID:")
        t_d = open("emp.csv","r").readlines()
        for row in t_d[2:]:
            each_row = row.split(',')
            if str(ID) == row.split(',')[0]:
                req_row = row
                ind = t_d.index(req_row)
                req_row = row.split(',')
                print req_row
                print "Current Available Info:", req_row
                Name = raw_input("Enter Name[{0}]:".format(req_row[1]))
                Age = raw_input("Enter Age [{0}]:".format(req_row[2]))
                Salary = raw_input("Enter Salary[{0}]:".format(req_row[3]))
                Status = raw_input("Enter Status[{0}]:".format(req_row[4].strip('\n')))
                if Name == '':
                    Name = row.split(',')[1]
                if Age == '':
                    Age = row.split(',')[2]
                if Salary == '':
                    Salary = row.split(',')[3]
                if Status =='':
                    Status = row.split(',')[4]
                t_d[ind] = row
            
        row ="{0},{1},{2},{3},{4}\n".format(ID,Name,Age,Salary,Status)
        
        f = open("emp.csv","w")
        f.writelines(t_d)
        f.close()
        print "\nModified Employee Information .."
        print "And Emp Info After Modifcation is:",row.strip('\n')
        
    elif select == '3' :
        flag=True
        ID = raw_input("Enter ID of Employee:")
        t_d = open("emp.csv","r").readlines()
        count1 = len(t_d)
        for i in range(1,count1):
            l_d=t_d[i].split(",")
            if l_d[0] == str(ID):
                l_d[4]= 'InActive'
                t_d[i] = ",".join(l_d)+"\n"
        f = open("emp.csv","w")
        f.writelines(t_d)
        f.close()
        print "Changed the Status of Employee to InActive"

    elif select == '1' :
        ID = raw_input("Enter ID of Employee:")
        t_d = open("emp.csv","r").readlines()
        count1 = len(t_d)
        if count1 == 1:
            print "No Records in the File .."
        flag = True
        for i in range(1,count1):
            l_d=t_d[i].split(",")
            if l_d[0] == str(ID):
                print "\nRequested Employee Information.."
                print "\nName of Employee: {0}\nAge: {1}\nSalary: {2}".format(l_d[1],l_d[2],l_d[3],l_d[4])
                flag = True
                break
            else:
                flag = False
        if flag == False:
            print "\nInvalid ID"
    elif select == '5':
        print "\nYou have Selected to Exit.."
        break
    else:
        print "\nSelect Appropriate Option\n"

    
        
    

    




##import random
##import os
##print "Options"
##print "1. Add a Row\n2. Modify a Row\n3. Delete a Row"
##select = raw_input("Select Any of the below Options:")
##
##if select == '1' :
##    if os.path.exists("D:\Python_Workspace\emp.csv"):
##        t_d = open("emp.csv","r").readlines()
##        persons = len(t_d)
##    else:
##        persons = 0
##    columns=['Id','Name','Salary']
##    age=range(23,60)
##    rows=[]
##    f = open("emp.csv","a")
##    rows.insert(0,",".join(columns)+"\n")
##    for i in range(10):
##        row = "{0},name{0},age{1}\n".format(i,random.choice(age))
##        rows.append(row)
##        f.writelines(rows)
##    print "Row Updated Successfully"
##        #f.close()
##if select == '2' :
##    id1 = 0
##    row ="{0},{1},{2}".format(id1,name,age)
##    t_d = open("emp.csv","r").readlines()
##    for row in t_d[2:]:
##        if str(id1) == row.split(',')[0]:
##            req_row = row
##    ind = t_d.index(req_row)
##    t_d[ind] = row
##    f = open("emp.csv","w")
##    f.writelines(t_d)
##    f.close()
##if select == '3' :
##    id1=2
##    t_d = open("emp.csv","r").readlines()
##    app =[]
##    for row in t_d:
##        if str(id1) == row.split(',')[0]:
##            print "Row:",row
##            t_d.remove(row)
##    f = open("emp.csv","w")
##    f.writelines(t_d)
##    #f.close()

    
        
    

    



