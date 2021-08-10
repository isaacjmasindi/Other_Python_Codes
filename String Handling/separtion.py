#seperation.py
#the program will request  the user to enter sentence 
#the split function used to split up the input(sentence)

sent_=input("please enter a sentence")

sent_2=sent_.split()

#the for loop will be used so that the split words  are in loop form as in one line after the other

for i in sent_2:
    print (i)