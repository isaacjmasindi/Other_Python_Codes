#bmi_task
#the program ask user to enter their information
height= float(input("Please enter your height in m :"))

print("Your current height is {}m".format(height))

weight=float(input("Please enter your weight in kgs"))

print("your current weight is {}kgs".format(weight))


#the height is squared
#the bmi is calculated 
# the if statment is used to detemined which group they fall under based on the bmi output
height_squ= (height*height)

Bmi= round(weight/height_squ,2)

if Bmi>=30:
    
    print("You are obese,your, currnt BMI is {}.".format(Bmi))

elif 30>Bmi>=25:
    
    print("You are overweight, your currnt BMI is {}.".format(Bmi))

elif 25>Bmi>=18.5:
    
    print("you are normal, your currnt BMI is {}.".format(Bmi))

elif Bmi<18.5:
    
    print("you are underweight, your currnt BMI is {}.".format(Bmi))
