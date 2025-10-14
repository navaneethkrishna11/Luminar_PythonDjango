import sqlite3
con= sqlite3.connect('school.db')
con.execute("""create table if not exists Student ( roll_no int primary key,name varchar(20),age int,gender varchar(20),course varchar(20),mark int)""")

def insert_student(r,n,a,g,c,m):
    con.execute("""insert into Student (roll_no,name,age,gender,course,mark) values(?,?,?,?,?,?)""",(r,n,a,g,c,m))
    con.commit()
    print('inserted')

def read_students():
    k=con.execute('select * from Student')
    print(k.fetchall())

def search_student(r):
    k = con.execute('select * from Student where roll_no=?',(r,))
    print(k.fetchall())

def update_mark(m,r):
    con.execute('update student set mark= ? where roll_no=?', (m,r))
    con.commit()
    print('updated')

def delete_student():
    con.execute('delete from student where roll_no=?',(r,))
    con.commit()
    print('deleted')
while 1:
    print("\n Menu Driven -DATABASE OPERATIONS")
    print(" 1.Insert student \n 2.Read all students \n 3.Search by Roll \n 4.Update Mark \n 5.Delete student \n 6.Exit")
    ch=int(input("choose : "))
    if ch==1:
        r=int(input("enter the roll : "))
        n=input("enter the name : ")
        a=int(input("enter the age : "))
        g=input("enter the gender :  ")
        c=input("enter the course : ")
        m=int(input("enter the marks : "))
        insert_student(r,n,a,g,c,m)
    elif ch==2:
        read_students()
    elif ch==3:
        r = int(input("enter the roll : "))
        search_student(r)
    elif ch==4:
        r = int(input("enter the roll : "))
        m=int(input("enter the marks : "))
        update_mark(m,r)
    elif ch==5:
        r = int(input("enter the roll : "))
        delete_student()
    elif ch==6:
        print('Thenkzzzz')
        break
    else:
        print('Invalid input')