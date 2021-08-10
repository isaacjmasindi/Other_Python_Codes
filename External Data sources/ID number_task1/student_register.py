# file idregs is opened to write the id numbers
#names takes in the number of students 
#for loop is used to run until the las number of the rang
#each id number is written in the fle 
with open ("reg_form.txt","w") as f:
    num_students=int(input("How many students are registering: "))
    
    for i in range(0,num_students):
        
        id_num=input("enter the ID number:")
        
        f.write('%s\n' % id_num)