import mysql.connector
# con=mysql.connector.connect(user='root',password='root',host='localhost')
#c=con.cursor()
# c.execute('create database shop')  #database creation
# print('db created')
con=mysql.connector.connect(user='root',password='root',host='localhost',database='shop')
c=con.cursor()

# c.execute('''create table Product (pid int primary key, pname varchar(20), price int) ''')
# print('table created')
# c.execute('''insert into Product values(1,'product A',200),(2,'product B',500),(3,'product C',1000),(4,'product D',3000)''')
# con.commit()

# c.execute('''create table Order_details(orderid int primary key, pid int , quantity int, ordered_date date, foreign key(pid) references Product(pid)) ''')
# print('table created')

# c.execute('''insert into Order_details values(100301,2,2,'2025-10-12'),(100302,4,4,'2025-10-16')''')
# con.commit()

