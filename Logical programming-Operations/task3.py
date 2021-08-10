#task3.py 
#the program request user to enter their completed times

print("Well done  for completeing our triathlon, kindly fill in the times you finished below")

swimming= float(input("please enter the time you completed in the swiming event"))

cycling= float(input("please enter the time you completed in the cycling event"))

running= float(input("please enter the time you completed in the running event"))


#All three variables are added to get the finish time for the triathlon
#the If statement is used to find out if the they have met the requirments to win and which level they won by 
triathlon= (swimming+cycling+running)
if triathlon<=100:

    print("you have obtained provincal colours")

elif 100<triathlon<=105:

    print("you have obatained provincial Half Colours")

elif 105<triathlon<=110:
    
    print("you have obtained provincial Scroll")

else:
    
    print("you have not obainted any award please try again next year")