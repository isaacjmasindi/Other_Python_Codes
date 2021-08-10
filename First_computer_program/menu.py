
# the program will request user to enter the food they want to order 
# after the user enters the food name it will show a message confirming the order
item1= input("Enter your first order of  food: ")
print(" You have successfully ordered  {} ".format(item1))
item2 = input("Enter your second  order of food:")
print(" You have successfully ordered {} ".format(item2))
item3 = input("Enter your third order of food:")
print(" You have successfully ordered {} ".format(item3))
# the program will display a message confirming all the orders made 
print("This is your ordered list: {},{} and {}".format(item1,item2,item3))