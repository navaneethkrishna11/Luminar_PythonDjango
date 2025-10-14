import sqlite3
con= sqlite3.connect('mydb.db')
# con.execute('create table Person(name varchar(20),age int)')
n=input("enter the name : ")
a=int(input("enter the age : "))
con.execute('insert into Person(name,age) values(?,?)',(n,a))
con.commit()

n=input("enter the name : ")
k=con.execute('select * from Person where name = ?',(n,))
print(k.fetchall())
