#the program imports the math module so i can make calculations in my code 
#the program imports statistice to find the median of the list
#the reseach for statistics were found on https://www.w3schools.com/python/module_statistics.asp
import math
import statistics
#the list_ varible has an empty list that the input will be added into
#the num varible is vauled to 0 and will be used to count the number of times the user gets to enter numbers
list_=[]
num=0
#the while loop will be used to keep asking the user to enter numbers until the length of numbers is equal to 10
while num!=10:
    numbers=input("Please enter any numbers with decimals or whole numbers")
    list_.append(numbers)
    num=num+1

#the each item in the list is converted to a float
# the length of the list is calclated
# the sum of the list is calucated and rounded off to two decimal 
# the max will return the highest number 
# the minimum number of the list is printed
# the average of the list will be calculated by the sum of the list and the length of the list  
#the median is returned through the statistics module
cont_str=[float(x)for x in list_]

length= len(cont_str)

total= round(sum(cont_str),2)

maxuim= max(cont_str)

minimum= min(cont_str)

average= round((total/length),2)

median= statistics.median(cont_str)

print(f"the total sum for the all the numbers is {  total}")

print(f"the maxuim number of the list is {maxuim}")

print(f"the minimum number of the list is {minimum}")

print(f"the average of the list is {average}")

print(f"the median of the list is {median}")





