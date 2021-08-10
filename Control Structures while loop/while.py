#while.py .
#the variable nums is valued to 0 so that it counts the number of each number entered
#inputs is a variable valued to 0 so that the each number entered can be added so that all the numbers enter
#the program request user to enter a number

nums=0

inputs=0

num=int(input("Plese enterany interger, only enter -1 when you would like to stop entering : "))

#the while loop is used to repeatedly ask the user to enter a number
#a calculation is made to sum up the total of the numbers entered
#a calculation is made to count the number of intergers entered

while num!=-1 :
    
    num=int(input("Plese enter any interger, only enter -1 when you would like to stop entering :"))
    
    inputs=inputs+num
    
    nums=nums+1

#once the user has entered -1 the average will be calculated
if num==-1:
    
    nums2=nums-1
    
    print("The average is {}.".format(inputs/nums2))