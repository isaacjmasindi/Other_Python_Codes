#task2
#the program user the user to enter year they would like to start with and the range of the of the years they would like to see if there are leap years or not 

start_year= int(input("Please enter the year you would like to start your leap year search from :"))

total_years= int(input("Please enter a number you would like to see the years for :"))

#the for loop is used to repeat the number of years  accorinding to what the user has entered 
# the range starts from the year they have entered and the year plus the number of times
# the leap year is calculated by divding the year by 4 and if there isnt any remainder then it is a leap year 

for year in range(start_year, start_year+total_years):
    
    if year % 4==0:
        print("{} is  a leap".format(year))
    else:
        print("{} isnt a lap".format(year))