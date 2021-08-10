#password.py
have_length=False

up_case=False

low_case=False

have_num=False

num_character=0


password_=input("Please enter a password :")

print("Thank you for entering password below, now please answer the questions below:")

length_check=input("Is your password longer than at least 6 characters(Yes or No) :")
if length_check=="Yes":
    have_length=True
else:
    print("Your password is not longer than 6 characters")

upcase_check=input("Does the password contain an upper case (Yes or No) :")
if upcase_check=="Yes":
    up_case=True
else:
    print("Your password does not conatin a upper case")

lowcase_check=input("Does the passwoard contain a lower case (Yes or No) :")
if lowcase_check=="Yes":
    low_case=True
else:
    print("Your password does not contain a lower case")

Havenum_check=input("Does the passwaord contain numbers (Yes or No) :")
if Havenum_check=="Yes":
    have_num=True
else:
    print("Your Password does not contain any numbers")

if have_length==True:
    num_character +=1

if up_case==True:
    num_character +=1

if low_case==True:
    num_character +=1

if have_num==True:
    num_character +=1

if num_character>=3:
    print("This is a suitable password")
else:
    print("This is not a suitable password please re-enter password")


    

