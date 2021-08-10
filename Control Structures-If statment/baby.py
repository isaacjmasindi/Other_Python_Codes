#baby.py
#the programe got the current date
import datetime

date_year=datetime.datetime.now()

#the program ask user to enter birth date and it is turned into an interger
birth_year=int(input("please enter your birth year:"))

#the current year is turned into and interger
date_year2=int(date_year.year)

#the current year minus the birth year to get age 
age=(date_year2-birth_year)

#the if statment is implamiated 
if age>=18:
    print("Congrats, you are old enough")



