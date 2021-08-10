#task3
#the while loop is used to count down numbers from 20 to 1 as long as the highest variable isnt lesser than 0
#the variable highest is valued to 20 which is the number we would like to start counting from
#the variable is then minused by 1 so we get the number lesser than the value by 1
highest=20

while highest>=0:
   
    print(highest)
   
    highest=highest-1
    

#the while loop is used to get all the even numbers from 0 to 22 by running as long as the even number is not gretater than 22
#the even variable is valued to 0 so that the while loop starts counting from 0
#to get only even numbers the varible is added by 2 which will only give us even numbers 
even=0

while even<22:
    
    print(even)
    
    even=even+2

#the while loop is used to keep on adding the dots until it reachers 5 dots
#the dots variable is valued to nothing as the first loop needs to start at 1
dots=""

while dots!=".....":
    
    dots=dots+"."
    
    print(dots)

#the program request the user to enter two intergers
#the for loop then while search for the gcd between 1 and the total number of the intergers 
#the for loop only stops once the gcd is found

import math

a= int(input("please enter your first postive interger"))

b= int(input("please enter your second postive interger "))

for i in range (1,b+1):
    
    if math.gcd(a,b)==i:
    
        print(i)
     
      