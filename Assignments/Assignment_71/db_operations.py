import sqlite3
class DB():
    def get_connection(self,database=None):
        database = database if database else "db_operations.db"
        con = sqlite3.connect(database)
        cur = con.cursor()
        return con,cur

    def create_table(self,name,age,gender,mobile):
        """query1 = "SELECT name FROM sqlite_master WHERE type='table' AND name='Register' "
        con,cur=self.get_connection()
        cur.execute(query1)
        con.commit()"""
        
        try:
            query="create table if not exists Register (R_ID INTEGER PRIMARY KEY AUTOINCREMENT,{0} varchar(250),{1} int,{2} char,{3} int)".format(name,age,gender,mobile)
            con,cur=self.get_connection()
            cur.execute(query)
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
            
    def insert_values(self,name,age,gender,mobile):
        try:
            con,cur=self.get_connection()
            cur.execute("insert into Register (Name,Age,Gender,Mobile) values (?,?,?,?)",(name,age,gender,mobile))
            r=cur.execute("select last_insert_rowid()")
            rid=r.fetchone()
            for i in rid:
                print "Now you are a registered member and your id is: {0}".format(i)
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()

