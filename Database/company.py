import sqlite3
con = sqlite3.connect('company.db')
# sql_command="""create table employee(empid int primary key,name varchar(20),age int,place varchar(20),salary int,gender varchar(20))"""
# con.execute(sql_command)
# print('success')
# sql_command1="""insert into employee(empid,name,age,place,salary,gender) values (100,'Navaneeth',21,'Tirur',23400,'male'),
# (101,'Amritha',19,'Cherpunkal',33400,'female'),(103,'Navitha',1,'Tirur',2,'female')"""
# sql_command1="""insert into employee(empid,name,age,place,salary,gender) values (104,'Nithin',22,'Tanur',34000,'male'),
# (105,'Malhotra',29,'Vaikom',33000,'male'),(106,'surya',30,'fidhu',56000,'male')"""
# con.execute(sql_command1)
# con.commit()
# print('insert')

k="""select * from employee"""
a=con.execute(k)
print(a.fetchall())
k="""select name,age from employee"""
a=con.execute(k)
print(a.fetchall())
k="""select * from employee where name='Amritha'"""
a=con.execute(k)
print(a.fetchall())
# q1
k="""select * from employee where empid=101"""
a=con.execute(k)
print(a.fetchall())
# q2
k="""select * from employee where salary>30000"""
a=con.execute(k)
print(a.fetchall())
# q3
k="""select * from employee where place='ekm'"""
a=con.execute(k)
print(a.fetchall())
# q4
k="""select * from employee where place!='ekm'"""
a=con.execute(k)
print(a.fetchall())
# q5
k="""select name,age,empid,salary from employee where empid=101"""
a=con.execute(k)
print(a.fetchall())

# limit and offset
k="""select * from employee limit 1 offset 1"""
a=con.execute(k)
print(a.fetchall())

# between
k="""select * from employee where age between 1 and 20"""
a=con.execute(k)
print(a.fetchall())

# in
k="""select * from employee where age in(1,29)"""
a=con.execute(k)
print(a.fetchall())

# in
k="""select * from employee where name like 'S%'"""
a=con.execute(k)
print(a.fetchall())

# 3 letter name starting with n
k="""select * from employee where name like 'n___'"""
a=con.execute(k)
print(a.fetchall())

# place starting with t
k="""select * from employee where place like 't%'"""
a=con.execute(k)
print(a.fetchall())

# place contains n
k="""select * from employee where place like '%n%'"""
a=con.execute(k)
print(a.fetchall())

# name contains n
k="""select * from employee where name like '%n%'"""
a=con.execute(k)
print(a.fetchall())

# 3 letter name contains n
k="""select * from employee where place like '_n_'"""
a=con.execute(k)
print(a.fetchall())

# 1).write a sql query to find the nobel prize winners for the year 1970(return year,subject and winner)
# select year,subject,winner from nobel_prize where year=1970;

# 2).write a sql query to find the nobel prize winnerin literature for 1971
# select * from nobel_prize where subject='literature' and year=1971;

# 3).sql to find the winners in the field of physics since 1978(return winner)
# select winners from nobel_prize where subject = 'physics' and year>=1978;

# 4)sql query to find the winners in chemistry between 1970 and 1980
# select winner from nobel_prize where subject='chemistry' and year between 1970 and 1980;

# 5)sql query to find the details of the winners whose firstname match with string 'Louis'
# select * from nobel_prize where winner like 'Louis%';

# 6).sql query to find the winners excluding subjects physiology and Economics.
# select winner from nobel_prize where subject not in ('physiology','Economics')

# Aggregate function
k="""select sum(salary),avg(salary),max(salary),min(salary) from employee """
a=con.execute(k)
print(a.fetchall())

# alter table employee rename coloumn to email;
# UPDATE employee set coloumn="naa@gmail.com" where empid=100;