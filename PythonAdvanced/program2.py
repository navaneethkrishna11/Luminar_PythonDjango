# read a file and append that file data to a new file.
# c
# a=f.read()
# f=open('a.txt','a')
# f.write( a)
# f.close()

#a+ mod operations (both read and write
# f=open('c.txt','a+')
# f.write('ohh come on')
# f.seek(0,0)  #added seek becz, the pointer is in last positon so to make it first
# s=f.read()
# print(s)

# delete a file
# import os
# os.remove('c.txt')

# Menu Driven Program
import os

def writeFile():
    f = open(file, 'w')
    wr = input("enter to write : ")
    f.write(wr)

def readFile():
    f = open(file, 'r')
    print(f.read())

def appendFile():
    f = open(file, 'a')
    a = input("enter text : ")
    f.write(a)

def searchWord():
    f = open(file, 'r')
    a = f.readlines()
    fin = input("enter the word : ")
    if fin in a:
        print("find")
    else:
        print("not find")

while True:
    print("1.Write File \t 2.Read File \t 3.Append File \t 4.Search a word in a file \t 5.Delete \t 6.Exit")
    ch = int(input("Enter the choice : "))
    if ch<6 :
        file=input("enter file name : ")
    if ch==1:
        writeFile()
    elif ch==2:
        readFile()
    elif ch==3:
        appendFile()
    elif ch==4:
        searchWord()
    elif ch==5:
        os.remove(file)
        print('File deleted')
    elif ch==6:
        print('exitingggg........')
        break
    else:
        print('invalidd')




