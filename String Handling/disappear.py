#disappear.py
#the program will request the user to enter a sentence and which characters they would like to remove
#the num varible will be counting the number of many times the loop will run
#the for loop be used run the loop until all the characters are removed
#once the number of loops is equal to length of the all the characters then the sentence will be printed
sent_=(input("please enter a sentence"))

disappear=(input("which characters of the sentence would you like to remove"))

num=0

sent_2=len(disappear)

for remove in disappear:
    
    sent_=sent_.replace(remove,"")
    
    num=num+1
    
    if num==sent_2:
            print(sent_)
