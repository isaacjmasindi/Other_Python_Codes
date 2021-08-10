#while loop
#the program request the user to enter any interger greater than 0 to be able to get even numbers from 1

num=int(input("Please enter greater then 0 :"))

#this varible carries a value of 0 as the calculation to get the even numbers need to start from zero

sum1 = 0                

#while loop is implaimented to keep calculating and showing the next even number until it reaches the user's interger then it will stop
while sum1<num:
     
     sum1=sum1+2
     
     print(sum1)