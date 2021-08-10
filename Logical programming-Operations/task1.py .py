#task1.py 
#assigned 3 numbers to 3 variables
num1= 400

num2= 1100

num4= 23

#the if and elif statement is implaimented to get the larger number between num1 and num2
if num1>num2:
    
    print(num1)

elif num2>num1:
    
    print(num2)

#the if and else stament is implaimented  to find out if the num2 is an odd or even number
if (num2 % 2)==0:
    
    print("even")

else:
   
    print("odd")

#the if statement and the AND condition  is used to sort the numbers from largest to smallest

if (num1>num2) and (num2>num4):
        print(num1,num2,num2)

if (num2>num4) and (num4>num1):
        print(num2,num4,num1)

if (num4>num1) and (num1>num2):
        print(num4,num1,num2)

if (num1<num2) and (num2<num4):
        print(num4,num2,num1)

if (num2<num4) and (num4<num1):
        print(num1,num4,num2)

if (num4<num1)  and (num1<num2):
        print(num1,num1,4)
