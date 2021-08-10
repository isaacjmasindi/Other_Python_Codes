#task.py
#the program request the user to enter any number they would like to see its timeable

timeable=int(input("Please enter any interger you would like to see its timesable"))

#the for loop is used to multipling the the number given by the user from the range if 1,13

for number_count in range(1, 13):
    print (timeable,"X",number_count,"=", timeable*number_count)
    
   