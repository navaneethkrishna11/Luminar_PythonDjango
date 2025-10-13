# Write a Python program using class methods and a looping menu to manage student records.
#
# Menu:
#
# 1. Add student (roll no,name, marks)
# 2. Display all students
# 3. Delete a student
# 4. Update marks of a student
# 5. Search student by name
# 6. Exit
class Students:
    def __init__(self):
        self.studid=int(input("enter the roll number : "))
        self.studname=input("enter the student name : ")
        self.studentsmarks=input("enter mark science : ")
        self.studentsmarkcs = input("enter mark computer science : ")
        self.studentsmarkcmaths = input("enter mark maths : ")

    def display(self):
        print("student name : ",self.studname,'| science mark :',self.studentsmarkcs,'| cs mark : ',self.studentsmarks,'| maths mark : ',self.studentsmarkcmaths,'|')

    def update(self):
        print('1.update name 2.update cs mark 3.update science mark')
        c = int(input("choose : "))
        if c == 1:
            self.studname = input("enter the student name : ")
        elif c==2:
            self.studentsmarks = input("enter mark science : ")
        elif c==3:
            self.studentsmarkcs = input("enter mark computer science : ")
        elif c==4:
            self.studentsmarkcmaths = input("enter mark maths : ")
s=[]
while 1:
    print('-----------------------------------------')
    print("\t S T U D E N T S  R E C O R D S ")
    print('----------------------------------------')
    print("|  1.Add student                       |")
    print("|  2.Display all students              |")
    print("|  3.Delete a student                  |")
    print("|  4.Update marks                      |")
    print("|  5.Search by student name            |")
    print("|  6.Exit                              |")
    print('------------------------------------------')
    ch=int(input("Enter the input :  "))
    if ch==1:
        a=Students()
        s.append(a)
    elif ch==2:
        if not s :
            print('no records !!')
        else:
            for i in s:
                i.display()
    elif ch==3:
        acn=int(input("enter delete , roll number :"))
        for i in s:
            if i.studid==acn :
                s.remove(i)
                print('removed!')
                break
    elif ch==4:
        acn=int(input("enter the roll number to update : "))
        for i in s:
            if i.studid==acn:
                i.update()
                print('updated!!')
                break

        print('not updated!!')
    elif ch==5:
        acn = input("enter the roll number to update : ")
        for i in s:
            if i.studname==acn:
                i.display()

        print('no user ')
    elif ch==6:
        print('thank u!')
        break
    else:
        print('invalid input ')

