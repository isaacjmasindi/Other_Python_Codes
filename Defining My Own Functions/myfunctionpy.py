#the days of the week function will print the days of the week
def days_week():
    print("Monday"",","Tuesday"",","Wednesday"",","Thursday"",","Friday")

#the replace function will split the sentence given by the user and if add the sentence to the a new variable 
#if the index of a certain word in the sentance is divisbale by 2 
def replacing():
    new_sent=""
    index=0
    for i in sentence.split():
        if index % 2!=0:
            new_sent+="hello"
        else:
            new_sent+=" "+ i + " "
        index+=1
    return new_sent





days_week()



sentence=input("please enter a sectence ")

print(replacing())


