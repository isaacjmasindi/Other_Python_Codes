#john.py
#the names varible has an empty list 
# the program ask the user to enter any name 
#the while loop is used to run as long the user hasnt entered the word john
#each name will be added into the names list 
# once the user enters john the loop will stop and the if statment is excuted to print out the list 
names=[]

name_search=input("Please enter your name: ")

while name_search.upper()!="JOHN":
    
    names.append(name_search)
    
    name_search=input("Please enter your name: ")
    
    if name_search.upper()=="JOHN":
        
        print(names)
