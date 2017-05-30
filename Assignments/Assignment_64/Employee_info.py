import sqlite3
class DB():
    def get_connection(self,database=None):
        database = database if database else "db_operations.db"
        con = sqlite3.connect(database)
        cur = con.cursor()
        return con,cur

    def create_table(self,tb_name,eid,ename,eage,eaddress,esal,eheight,eweight):
        try:
            con,cur=self.get_connection()
            query="create table EMPLOYEE({0} varchar(5),{1} varchar(250),{2} int,{3} varchar(260),{4} int,{5} float,{6} float)".format(eid,ename,eage,eaddress,esal,eheight,eweight)       
            cur.execute(query)
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()

    def insert_values(self,eid,ename,eage,eaddress,esal,eheight,eweight):
        try:
            con,cur=self.get_connection()
            cur.execute("insert into EMPLOYEE (ID,Name,Age,Address,Salary,Height,Weight) values (?,?,?,?,?,?,?)",(eid,ename,eage,eaddress,esal,eheight,eweight))
            con.commit()
            print "Inserted Values"
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()

    def Get_Emp_Info(self,eid):
        try:
            con,cur = self.get_connection()
            cur.execute("select Name,Age,Address,Salary,Height,Weight from EMPLOYEE where ID=?",(eid,))
            l=cur.fetchone()
            print "Name:",l[0]
            print "Age:",l[1]
            print "Address:",l[2]
            print "Salary:",l[3]
            print "Height:",l[4]
            print "Weight:",l[5]
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()

    def Get_Sal(self):
        try:
            con,cur = self.get_connection()
            cur.execute("select AVG(Salary) from EMPLOYEE")
            l=cur.fetchone()
            print "Average Salary:",l[0]
            
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
    def High_Sal(self):
        try:
            con,cur = self.get_connection()
            cur.execute("select Age, Address, Salary FROM EMPLOYEE WHERE Salary = (SELECT Max(Salary) FROM EMPLOYEE)")
            l=cur.fetchone()
            print "Highest Salary is:",l[2]
            print "Age of Person who is seeking Highest Salary is:",l[0]
            print "Address of Person who is seeking Highest Salary is:",l[1]
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
    def BMI_Val(self):
        try:
            con,cur = self.get_connection()
            cur.execute("select ID,(Weight)/((Height/100)* (Height/100))FROM EMPLOYEE")
            l=cur.fetchall()
            for i in l:
                print "Employee {0} BMI Value is: {1}".format(i[0],i[1])
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
    def Overall_BMI_Val(self):
        try:
            sum1=0
            count =0
            con,cur = self.get_connection()
            cur.execute("select ID,(Weight)/((Height/100)* (Height/100))FROM EMPLOYEE")
            l=cur.fetchall()
            for i in l:
                #print i[1]
                count = count+1
                sum1 = sum1+i[1]
            #print "Sum",sum1
            print "Overall BMI:",sum1/count
                #print "Employee {0} BMI Value is: {1}".format(i[0],i[1])
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
        
        
                        
            
 
            
            
