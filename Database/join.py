# create table Author(author_id int primary key , author_name varchar(20),nationality varchar(20),birthyear int);
# insert into Author values(1,'ayush','indian',2000),(2,'biji','usa',2001),(3,'suresh','italy',2001);
#
# create table Books(bookno int primary key, title varchar(20),author_id int, price int, pages int, published_year int, foreign key(author_id) references Author(author_id));
# insert into Books values(100,'AOT',1,200,242,2021),(101,'One piece',1,3450,300,2000),(102,'Naruto',2,3040,10,200);
#
#
# -- 1,Find all books of specific author
# select * from Author join Books on Author.author_id = Books.author_id where author_name='ayush';
# -- 2.Find the publication year of a particular book
# select published_year from Books where bookno=100;
# -- 3.Find the youngest author
# select author_name,birthyear from Author Order by birthyear desc limit 1 ; #not feasible , single value only
# select author_name from Author where birthyear=(select Max(birthyear) from Author);
# -- 4.List books with their corresponding author where booktitle contains a specific keyword
# select Books.bookno,Author.author_name from Books join Author on Books.author_id=Author.author_id where Books.title like 'Naruto%';
# -- 5.list all authors who have written books published after a particular year
# select distinct(Author.author_name) from Author join Books on Author.author_id= Books.author_id where Books.published_year>2000;