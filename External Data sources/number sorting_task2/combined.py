
#i opened a file named number1.txt
#4 variables with intergers 
 
with open("numbers1.txt","w") as f:
    num1=3
    
    num2=16
    
    num3=77
    
    num4=200
     
#the intergers are written into the file 
#each interger is written on a new   
    
    f.write(str('%s\n' %num1))
    
    f.write(str('%s\n' %num2))
    
    f.write(str('%s\n' %num3))
    
    f.write(str('%s\n' %num4))

#i opened a file named number1.txt
#4 variables with intergers 
with open("numbers2.txt","w") as f:
    num1=20
    
    num2=93
    
    num3=400
    
    num4=600

#the intergers are written into the file 
#each interger is written on a new       
    
    f.write(str('%s\n' %num1))
    
    f.write(str('%s\n' %num2))
    
    f.write(str('%s\n' %num3))
    
    f.write(str('%s\n' %num4))



#the numbers1.txt file is opened to only read information
#a new variable is created to read, strip, split information from the file
#the information is converted into an interger from string

with open("numbers1.txt","r") as f:
        new2= f.read().strip().split("\n")
        convert_str=[int(x)for x in new2]
    
#the numbers1.txt file is opened to only read information
#a new variable is created to read, strip, split information from the file
#the information is converted into an interger from string

with open("numbers2.txt","r") as f:
        new2= f.read().strip().split("\n")
        convert_str2=[int(x)for x in new2]

#i joined conver_str2 into convert_str which joins the list
#the list is sorted from smallest to largest   
convert_str.extend(convert_str2)
convert_str.sort()

#the numbers1.txt file is opened to only read information

with open("all_number.txt","w") as f:
    f.write(str(convert_str))


































