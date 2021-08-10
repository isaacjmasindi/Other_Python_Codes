#task2.py
#the proram request user to enter a information
shape=input("please enter the shape you would like the building to be(square, rectangular or circle) :")

#the if statment is implamented 
#a new variable is created to store the length
# area is calculated 

if shape=="square":

    length_squ= float(input("please enter the length in meters:"))

    area_squ= (length_squ*length_squ)

    print("The area for the square is {} units squared ".format(area_squ))

#elif statement is implaimented  for the rectangular if the if statment doesnt go through
# a new variable for  length and width is created to store the measurements
#the area is calculated and print out a message 

elif shape=="rectangular":

    length_rec= float(input("Please enter length :"))

    width_rec= float(input("please enter width :"))

    area_rec= round(length_rec*width_rec,2)

    print("The area for the rectangular is {} units squared".format(area_rec))
#elif statement is implaimented  for the circle if the if statment doesnt go through
# a new variable of radius is created to store  length of the radius
# the radius is then multipled by itself 
#pi variable is created 
# the area is calculated and print out a message 


elif shape=="circle":

    radius_cir= float(input("Please enter the radius length of the circle:"))

    radius_2= (radius_cir*radius_cir)

    pi=3.14

    area_cir= (pi*radius_2)

    print("The area for the circle is {} units squared".format(area_cir))
    