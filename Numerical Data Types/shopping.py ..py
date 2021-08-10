#shopping.py 
#the program request the user information
product_name1=input("please enter name of first product:")

product_price1=float(input("please enter price of first product:"))

convert="{:.2f}".format(product_price1)

print("the price of {} is R{}".format(product_name1,convert))

product_name2=input("please enter name of second product:")

product_price2=float(input("please enter price of second product:"))

convert1="{:.2f}".format(product_price2)

print("the price of {} is R{}".format(product_name2,convert1))

product_name3=input("please enter name of third product:")

product_price3=float(input("please enter price of third product:"))

convert2="{:.2f}".format(product_price3)

print("the price of {} is R{}".format(product_name3,convert2))

#the the total sum of all the products 
total_sum=(product_price1+product_price2+product_price3)

convertsum="{:.2f}".format(total_sum)

#the average of the all products 

average=float(total_sum/3)

two_decimal=round(average,2)

# print of all the all products,total sum and average
print( "The total of {}, {}, {} is R{} and the average price of the items is R{}".format(product_name1,product_name2,product_name3,convertsum,two_decimal))




