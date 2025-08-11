student_grades = {'Alice':90,'Bob':85,'Charlie':74,'Mike':70}
# print grad of charlie
print('CHARLIE : ',student_grades['Charlie'])
# update the grade of bob to 90
student_grades['Bob']=90
# add new item 'sam':75 to the dic
student_grades['Sam']=75
# print the total number of students in the dict
print("length of students",len(student_grades))
# print all student names from the dict
print('Student Name:',student_grades.keys())

# 2. Given a list
colors = ['red','green','yellow']
# add new color black
colors.append('black')
#  update 2nd index to blue
colors[2] = 'blue'
print(colors)

# 3.Given a set
s = {'guitar','veena','drums'}
# add new item flute to set
s.add('flute')
print(s)