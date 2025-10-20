import mysql.connector

# con=mysql.connector.connect(user='root',password='root',host='localhost')
# connect to the server
# print(con)
# c=con.cursor()  #creating cursor obj for executing sql commands

# c.execute('create database company')  #database creation
# print('db created')

# con=mysql.connector.connect(user='root',password='root',host='localhost',database='company')
# c=con.cursor()
# c.execute('''create table employee (empid int primary key, name varchar(20), age int, place varchar(20),gender varchar(20),salary int  ) ''')
# print('table created')
# c.execute('''insert into employee values(100,'abin',22,'vaikom','male',20000),(101,'shankar',22,'kanjirapally','male',35000),(102,'abhiram',26,'pala','male',64000),(103,'anjaly',28,'tirur','female',10000),(104,'banu',24,'kozhikode','female',20600)''')
# con.commit()
# print('data inserted')

# to read data from database
# c.execute('select * from employee')
# k=c.fetchall()
# print(k)

# dynamic input
# id=int(input("enter the id : "))
# n=input("enter the name : ")
# a=int(input("enter the age : "))
# p=input("enter the place : ")
# g=input("enter the gender : ")
# s=int(input("enter the salary : "))
# c.execute('insert into employee values(%s,%s,%s,%s,%s,%s)',(id,n,a,p,g,s))
# con.commit()
# print('inserted')


# c.execute('create database hotel')  #database creation
# print('db created')
con=mysql.connector.connect(user='root',password='root',host='localhost',database='hotel')
c=con.cursor()

# c.execute('''create table Product (pid int primary key, pname varchar(20), price int) ''')
# print('table created')
# c.execute('''insert into Product values(1,'product A',200),(2,'product B',500),(3,'product C',1000),(4,'product D',3000)''')
# con.commit()

# c.execute('''create table Order_details(orderid int primary key, pid int , quantity int, ordered_date date, foreign key(pid) references Product(pid)) ''')
# print('table created')

c.execute('''insert into Order_details values(100301,2,2,'2025-10-12'),(100302,4,4,'2025-10-16')''')
con.commit()