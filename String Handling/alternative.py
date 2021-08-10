#alternative.py
#the program request user to enter a sentence
#the new_sent varible is valued to nothing currently
string=input("please enter a sentence")

new_sent=""

#the for loop will check the range between 0 and the length of the sentence
#for every number in the lenth that is divisable by 2 and leaves no remainder the it will be upper case and those that are not diviable will be lower case
#each character will be stored in the new_sent variable unitl the loop stop
for i in range(0,len(string)):
    
    if i%2==0:
        new_sent+=string[i].upper()
    
    else:
        new_sent+=string[i].lower()

print(new_sent)
