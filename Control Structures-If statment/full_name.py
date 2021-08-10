#full_name.py
#the program request the user to enter info
name=input("what is your full name?")

#the length of the input
length=len(name)

#the IF statment 
if length==0:

    print("You haven’t entered anything. Please enter your full name.”")
   

if 0<length<=3:

    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname")
    

if length>25:

    print("You have entered more than 25 characters. Please make sure that you have only entered your full name")

#print the output
if 4<=length<=25:

    print("Thank you for entering your name")
    

    
    
        