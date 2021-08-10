
#the min function will output the minimun number in the list
def min_():
    min_2=min(convert)
    return  min_2

#the max fuction will output the max number in the list
def max_():
    max_2=max(convert2)
    return  max_2

# the avg function will output the avgerage of the list
def avg():
    avg_2=sum(convert3)/len(convert3)
    return avg_2





#the the string list is turned into a list
with open("input.txt","r") as f:
    lines=f.readlines()
    
    list_1=lines[0].strip().split(":")
    new_list=list_1[1].split(",")
    convert=[int(x) for x in new_list]
    
    list_2=lines[1].strip().split(":")
    new_list2=list_2[1].split(",")
    convert2=[int(x) for x in new_list2]
    
    list_3=lines[2].strip().split(":")
    new_list3=list_3[1].split(",")
    convert3=[int(x) for x in new_list3]
    

#all the functions are now stored into new variables 
    
    max_num=max_()
    
    min_num=min_()
    
    avg_num=avg()

# the output from the functions will be written into the output.txt fle 
with open("output.txt", "w") as f2 :
    f2.write(f"The min of {convert} is {min_num}\nThe max of {convert2} is {max_num}\nThe average of {convert3} is {avg_num}") 
