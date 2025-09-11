# #Library Management system
class Book:
    def __init__(self):
        # self.acctnumber=0
        # self.acctname=""
        # self.balance=0
        self.books = []

    def create(self):
        try:
            booknumber=int(input("enter the number :  "))
            for i in self.books:
                if booknumber == i[0] :
                    print('Already Book Added')
                    return

            booktitle = input("Enter Book Title : ")
            bookauthor = input("Enter Author Name : ")
            bookprice = int(input("Enter Book Price : "))
            bookpages = int(input("Enter Book Pages : "))
            booklang = input("Enter Book Languages : ")
            self.books.append([booknumber,booktitle,bookauthor,bookprice,bookpages,booklang])
            print('New Book Added !!')
        except Exception as e:
            print(e)

    def update(self):
        try:
            br=int(input("enter the book number : "))
            for i in self.books:
                if  i[0] == br:
                    print('choose update : 1. title 2.author 3.price 4.pages 5.language')
                    a=int(input("enter : "))
                    if a==1:
                        i[1]=input("enter the title : ")
                    elif a==2:
                        i[2]=input("enter the author name : ")
                    elif a==3:
                        i[3]=int(input("enter the price : "))
                    elif a==4:
                        i[4]=int(input("enter the pages : "))
                    elif a==5:
                        i[5]=input("enter the langugaes : ")
                    print('Successfully updated!!')
                    return

            print('No books Found!!')
        except Exception as e:
            print(e)

    def delete(self):
        try:
            br = int(input("enter the book number : "))
            for i in self.books:
                if i[0] == br:
                    self.books.remove(i)
                    print('Successfully deleted!!')
                    return

            print('No Book Found!!')
        except Exception as e:
            print(e)

    def showallbook(self):
        for i in self.books:
            print('Book Names : ',i[1])
            return
        print('Nothing to show!!')

    def showperbook(self):
        br=int(input("enter the book id : "))
        for i in self.books:
            if br==i[0]:
                print(i[1],i[2],i[3],i[4],i[5])
                return
        print('No book in this id!!')


b = Book()
while 1:
    try:
        print("-----------------------")
        print('| \t\tLibrary       |')
        print("-----------------------")
        print("| 1.Add a Book         |")
        print("| 2.Show all Book      |")
        print("| 3.Show perticular bk |")
        print("| 4.Update a book      |")
        print("| 5.Delete a book      |")
        print("| 6.Exit               |")
        print("-----------------------")
        ch=int(input("Choose :"))
        if ch==1:
            b.create()
        elif ch==2:
            b.showallbook()
        elif ch==3:
            b.showperbook()
        elif ch==4:
            b.update()
        elif ch==5:
            b.delete()
        elif ch==6:
            break
        else:
            print("Invalid input ")
    except Exception as e:
        print(e)



# Method teached by miss!!!
class Book:
    def __init__(self, booknumber, booktitle, bookauthor, bookprice, bookpages, booklang):
        self.booknumber = booknumber
        self.booktitle = booktitle
        self.bookauthor = bookauthor
        self.bookprice = bookprice
        self.bookpages = bookpages
        self.booklang = booklang

    def update(self):
        print('choose update : 1. title 2.author 3.price 4.pages 5.language')
        a = int(input("enter : "))
        if a == 1:
            self.booktitle = input("enter the title : ")
        elif a == 2:
            self.bookauthor = input("enter the author name : ")
        elif a == 3:
            self.bookprice = int(input("enter the price : "))
        elif a == 4:
            self.bookpages = int(input("enter the pages : "))
        elif a == 5:
            self.booklang = input("enter the language : ")
        print("Successfully updated!!")

    def show(self):
        print(self.booknumber, self.booktitle, self.bookauthor, self.bookprice, self.bookpages, self.booklang)


books = []
while 1:
    try:
        print("-----------------------")
        print('| \t\tLibrary       |')
        print("-----------------------")
        print("| 1.Add a Book         |")
        print("| 2.Show all Book      |")
        print("| 3.Show particular bk |")
        print("| 4.Update a book      |")
        print("| 5.Delete a book      |")
        print("| 6.Exit               |")
        print("-----------------------")
        ch = int(input("Choose : "))
        if ch == 1:
            booknumber = int(input("Enter the number : "))
            for b in books:
                if b.booknumber == booknumber:
                    print("Already Book Added")
                    break
            else:
                booktitle = input("Enter Book Title : ")
                bookauthor = input("Enter Author Name : ")
                bookprice = int(input("Enter Book Price : "))
                bookpages = int(input("Enter Book Pages : "))
                booklang = input("Enter Book Languages : ")
                b = Book(booknumber, booktitle, bookauthor, bookprice, bookpages, booklang)
                books.append(b)
                print("New Book Added !!")
        elif ch == 2:
            b.show()
        elif ch == 3:
            br = int(input("Enter the book id : "))
            for b in books:
                if b.booknumber == br:
                    b.show()
                    break
            else:
                print("No book in this id!!")
        elif ch == 4:
            br = int(input("Enter the book id : "))
            for b in books:
                if b.booknumber == br:
                    b.update()
                    break
            else:
                print("No book in this id!!")
        elif ch == 5:
            br = int(input("Enter the book id : "))
            for b in books:
                if b.booknumber == br:
                    books.remove(b)
                    print("Successfully deleted!!")
                    break
            else:
                print("No book in this id!!")
        elif ch == 6:
            break
        else:
            print("Invalid input ")
    except Exception as e:
        print(e)
