import sqlite3
class DB():
    def get_connection(self,database=None):
        database = database if database else "db_operations.db"
        con = sqlite3.connect(database)
        cur = con.cursor()
        return con,cur

    def  create_table(self,tb_name,name,age,sex,mobile):
        try:
            query="create table if not exists {0}(R_ID INTEGER PRIMARY KEY AUTOINCREMENT,{1} varchar(250),{2} int,{3} char,{4} int)".format(tb_name,name,age,sex,mobile)
            
            con,cur=self.get_connection()
            cur.execute(query)
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()

    def insert_values(self,tb_name,name,age,sex,mobile):
        try:
            con,cur=self.get_connection()
            cur.execute("insert into %s (Name,Age,Sex,Mobile) values (?,?,?,?)"%tb_name,(name,age,sex,mobile))
            r=cur.execute("select last_insert_rowid()")
            rid=r.fetchone()
            con.commit()
            print "Now you are a registered member and your id is {0}".format(rid)
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
            
    def update_values(self,tb_name,rid,mobile):
        try:
            con,cur=self.get_connection()
            print "Updated Mobile",mobile
            cur.execute("update %s SET Mobile=? WHERE R_ID=?"%tb_name,(mobile,rid))
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
            
    def delete_values(self,tb_name,rid):
        try:
            con,cur=self.get_connection()
            cur.execute("delete from %s WHERE R_ID = ?;"%tb_name,(str(rid)))
            con.commit()
        except Exception as err:
            print err
        finally:
            cur.close()
            con.close()
    def insert_dummy_data():
        try:
            con,cur = get_connection()
            for i in range(1000):
                q="insert into Register values({0},'name{0}')".format(i)
                cur.execute(q)
        except Exception as err:
            print err
        else:
            con.commit()
        finally:
            cur.close()
            con.close()


