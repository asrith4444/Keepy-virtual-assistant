import sqlite3
d=sqlite3.connect("emp.db")
d.execute('''create table if not exists sigdb1(fname varchar2(20),lname varchar2(20),uname varchar2(10) unique,pwd varchar2(20))''')
#print("Table Created")

def insert(fname,lname,uname,pwd):
    d.execute('''insert into sigdb1 values(?,?,?,?)''',(fname,lname,uname,pwd))
#insert('','','','')
d.commit()
