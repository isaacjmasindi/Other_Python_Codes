#list_types.py
# a message is printed informaing of whats on the next line 

print("These are my friend's names:")

#the friends variable is a list that contains all the names 
#num is a varible that contains the length of friendslist
#the first and second name is printed and the length of the friends list
friends=['Collin','Wezi','Owen']

num=len(friends)

print("the first friend is {} and the last friend is {}.The length of list is {}.".format(friends[0],friends[2],num))


# a message is printed informaing of whats on the next line 
#friend's age varible is list that contains the ages of my friends
#new_list is list that contains both the friends and friend's age list
#the list are printed in a corresponding way that the index match

print("\n")

print("These are my friend's age:")

friends_ages=[21,23,20]

new_list=[friends,friends_ages]

print(f"{new_list[0][0]} is {new_list[1][0]} years old\n{new_list[0][1]} is {new_list[1][1]} years old\n{new_list[0][2]} is {new_list[1][2]} years old.")








          