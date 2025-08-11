# create a list of 5 food items
food = ["biriyani","alfham","shawaya","burger","shawarma"]
# add a new thing to the list
food.append("mandi")
# update the 2nd food item to new value
food[1] = 'meals'
# print updated list
print(food)
# print the length of list
print("length of food item : ", len(food))
# print reverse of the list
print("reverse : ", food[::-1])
# print the last food item
print("last fd item : ",food[-1])
# print 5th food item
print("fifth food item : ",food[4])

l = [23,56,89,10,67,45,17]
l[1], l[5] = l[5],l[1]
print("New swapped array : ", l)
