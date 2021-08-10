#manipulation.py .
#the program request user for input
str_manip=input("please define a friendship?")
#the length of the input
print(len(str_manip))
#find and change the last character to @
str_manip2=(str_manip[-1])
print(str_manip.replace(str_manip2,'@'))
#print the last 3 characters backwards
str_manip3=str_manip[-3:]
str_manip4=str_manip3[::-1]
print(str_manip4)
#create a five letter word))
str_manip5=str_manip[0:3]
str_manip6=str_manip[-2:]
str_manip7= str_manip5+str_manip6
print(str_manip7)
#Display each word on a new line
print(str_manip.replace(" ","\n"))
