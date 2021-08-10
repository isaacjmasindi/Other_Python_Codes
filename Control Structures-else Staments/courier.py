#courier.py
#the program request user to enter data

package_price_=float(input("Please enter the price of the package you would like to purchase:"))

delivery_distance=float(input("Please enter the total distance of the delivery in kms:"))


#the calculations of the distance when a air or frieght delivery is used 
#the user gets to choice bewtween the two(Air or frieght)
Air=(delivery_distance*0.36)

Frieght=(delivery_distance*0.25)

delivery_choose=input("Would you like your delivery to be by (Air or Frieght):")
if delivery_choose=="Air":
    delivery1=Air
else:
    delivery1=Frieght

print("You have chosen the the {} delivery option.".format(delivery_choose))


#the user gets to choose what typye of insurance they want between these two(Full or Limited)
Full=50.00

limited=25.00

insurance=input("What type of insurance would you like (Full or Limited):")
if insurance=="Full":
    package_insure=Full
else :
    package_insure=limited

print("You have chosen the the {} insurance option.".format(insurance))


#the users must choose whether they want a gift or not
gift=15.00

No_gift=0.00

gift_Check=input("What type of insurance would you like (Gift or No Gift):")
if gift_Check=="Gift":
    gift_chose=gift
else :
    gift_chose=No_gift

print("You have chosen the the {} option.".format(gift_Check))


#the user must choose whether they want their delivery to be a priority or standard delivery
priority=100.00

standard_delivery=20.00

type_delivery=input("What type of insurance would you like (Priority or Standard delivery):")
if type_delivery=="Priority":
    type_1=priority
else :
    type_1=standard_delivery

print("You have chosen the the {} option.".format(type_delivery))


#the total cost everyting combined together
total_cost=(delivery1+package_insure+gift_chose+type_1)
total_convert=round(total_cost,2)
print("Thank you for choosing us , your total price is R{}".format(total_convert))









   




