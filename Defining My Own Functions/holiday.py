#the hotel function will calucate how much the user will have to pay based on the number of nights they are staying
def hotel_cost(num_nights):
    return num_nights*500.00

#the plane_cost function will charge the user an amount based on the choice of the  airport they will be landing at 
def plane_cost(airport_choice):
    if airport_choice.upper()=="A":
        airport_choice=500
    elif airport_choice.upper()=="B":
        airport_choice=1000
    elif airport_choice.upper()=="C":
        airport_choice=1500
    return airport_choice

# the type car function will charge the user an amount based on the choice of the type of car they want 
def type_car(car):
    if car.upper()=="A":
        car=200
    elif car.upper()=="B":
        car=450
    elif car.upper()=="C":
        car=700
    elif car.upper()=="D":
        car=1200
    return car

#the car_rental function will calucate how much the user will have to pay to use the car based on the number of days they will be using the car 
def car_rental(num_days):
    return num_days

#the holiday_cost fuction will calculate the total cost of the trip
#if the user stays for more than 10 days they will recive a 500 discount 
def holiday_cost(num_nights,airport_choice,num_days,car):
    if num_nights>=5000:
        return num_nights+airport_choice+(num_days*car)-500
    elif num_nights<5000:
        return num_nights+airport_choice+(num_days*car)


print("Welcome to travel-With-Us")

print("\n")

print("NB:please note we have a discount for those that choose to stay longer than 10 days at our accomdation")

num_nights=int(input("Please enter the number of days you be staying with us: "))

airport_choice=input("Please choose which airport you be flying to\nA.London Heathrow Airport\nB.London Gatwick Airport\nC.Manchester airport\n:")

num_days=int(input("Plese enter the number of days you will be renting the car for: "))

car=input("Please choose which type of car you would like to rent\nA.Small car\nB.4x4\nC.Kombi\nD.Sports car")

#the functions are now stored into varibles
num_nights=hotel_cost(num_nights)
airport_choice=plane_cost(airport_choice)
num_days=car_rental(num_days)
car=type_car(car)
total=holiday_cost(num_nights, airport_choice,num_days,car)

#the function is called and the total of the trip is printed
print(f"the total cost of your trip will be R{holiday_cost(num_nights, airport_choice,num_days,car)}")
 

