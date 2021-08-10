#control.py
#the user is requested to enter informaation 
age= int(input("Please enter your age "))

#the if statment is used to determine which catorey they fall under
if age>=18:
    
    print("you are old enough")

elif 16<=age<18:
    
    print("you are almost there")

else:
    
    print("you are just to young")
