
#the program request the user to enter a sentece 
#the replace function then replaces empty spaces with nothing so all the words are on
user_input= input("Please enter a sentence:")

new_sentence=user_input.replace(" ","")
# words_dict is a varible that has an empty list
#the for loop will run in way that will if a letter appears more than once in the word_dict dictionary it will keep adding 1 to the letter if not it will just remain at one 
words_dict={}

for i in new_sentence:
    if i in words_dict:
        words_dict[i]+=1
    else:
        words_dict[i]=1

print(str(words_dict))