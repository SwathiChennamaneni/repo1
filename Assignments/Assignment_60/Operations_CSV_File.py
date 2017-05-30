"""60. Show the below menu to the user:
     1. Add a row
     2. modify a row
     3. delete a row
     Go with one unique field in the file. And maintain that unique constraint in all file modifiction operations
     Use .CSV file for this program"""

import random
import os
import sys
select = True

while select:
    print "\n***** Menu *****"
    print "1. Add a Row\n2. Modify a Row\n3. Delete a Row\n4. Quit"
    select = raw_input("\nSelect:")

    if not os.path.exists("D:\py_programs\Assignments\Assignment_60\csv1_op.csv"):
        columns=['Id','Name','Age','Class','Rank']
        f = open("csv1_op.csv","w")
        rows=[]
        rows.insert(0,",".join(columns)+"\n")
        f.writelines(rows)
        f.close()
        last = 1
    else:
        t_d = open("csv1_op.csv","r").readlines()
        count = len(t_d[1:])
        if count:
            last = int(t_d[count][0]) + 1
        else:
            last = 1

    if select == '1' :
        #ID = last + int(1)
        Name = raw_input("Enter Name:")
        Age=raw_input("Enter Age:")
        Class = raw_input("Enter Class:")
        Rank = raw_input("Enter Rank:")
        rows=[]
        f = open("csv1_op.csv","a")
        row = "{0},{1},{2},{3},{4}\n".format(last,Name,Age,Class,Rank)
        rows.append(row)
        f.writelines(rows)
        print "Added Students Info in to a Row"
        print "Row/Student Id is:",last
        f.close()
        
    elif select == '2':
        ID = raw_input("Enter ID:")
        t_d = open("csv1_op.csv","r").readlines()
        for row in t_d[2:]:
            each_row = row.split(',')
            if str(ID) == row.split(',')[0]:
                req_row = row
                #print req_row
                ind = t_d.index(req_row)
                req_row = row.split(',')
                print "Current Available Info:", req_row
                Name = raw_input("Enter Name[{0}]:".format(req_row[1]))
                Age = raw_input("Enter Age [{0}]:".format(req_row[2]))
                Class = raw_input("Enter Class[{0}]:".format(req_row[3]))
                Rank = raw_input("Enter Rank[{0}]:".format(req_row[4].strip('\n')))
                if Name == '':
                    Name = row.split(',')[1]
                if Age == '':
                    Age = row.split(',')[2]
                if Class == '':
                    Class = row.split(',')[3]
                if Rank =='':
                    Rank = row.split(',')[4]
           
            row ="{0},{1},{2},{3},{4}\n".format(ID,Name,Age,Class,Rank)
            t_d[ind] = row
            f = open("csv1_op.csv","w")
            f.writelines(t_d)
            f.close()
        print "\nModified Row/Student Information .."
        
    elif select == '3' :
        flag=True
        ID = raw_input("Enter ID of Employee:")
        t_d = open("csv1_op.csv","r").readlines()
        count1 = len(t_d)
        for row in t_d:
            if str(ID) == row.split(',')[0]:
                print "Row:",row
                t_d.remove(row)
        f = open("csv1_op.csv","w")
        f.writelines(t_d)
        f.close()
        print "Deleted Students Information"

    elif select == '4':
        print "\nYou have Selected to Exit.."
        break
    else:
        print "\nSelect Appropriate Option\n"
    
        
    

    



