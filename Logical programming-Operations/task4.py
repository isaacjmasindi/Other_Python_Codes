#task4.py .
#the program requeest user to enter any interger
divisible= int(input("Please enter any interger "))

print("This is the interger you have entered {}".format(divisible))

#if statement is used to detemine true or false 
#the Modulus is used to see whether the interger is divisible
if (divisible%2==0) and (divisible%5==0):

    print("This interger is divisible by both 2 and 5")

elif (divisible%2==0) or (divisible%5==0):

    print("This interger is only divisible by 2 or 5 ")

elif not(divisible%2==0) or not(divisible%5==0):

    print("This interger is not divisible by niether 2 or 5")
