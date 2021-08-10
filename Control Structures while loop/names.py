#name.py
#the program request the user to enter the student's names and type stop when shes done
#a variable is cretated valued to 0 so that everytime a name is entered it counts and adds 

names= input("Please enter the name of your students and type stop to indicate that the names of all the students have been entered :")

num_names= 0

#the while loop is used so that the teacher can enter the names of all the students until they enter stop when they are done 
#everytime a name is entered it is considered as +1 so that the program can count the amount of names entered 

while names.upper() != "STOP":

    num_names= num_names+1
    
    names= input("Please enter the name of your students and type stop to indicate that the names of all the students have been entered: ")

#once the user enters stop it will print the number of names which represents the number

if names.upper()=="STOP":
    
    print("the num of students is {}".format(num_names))

    