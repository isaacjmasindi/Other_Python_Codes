#the random module is imported
#jokes is a list that contains the jokes
#the random moudle is used with randint to show random jokes of the list from index 0 to index -1
#the random module reseach https://www.w3schools.com/python/module_random.asp
import random
# the jokes were found on https://www.rd.com/jokes/
jokes= ["Why did the gym close down? It just didn’t work out","You know what I saw today? Everything I looked at","If we shouldn’t eat at night, why do they put a light in the fridge?","I tried to sue the airport for misplacing my luggage. I lost my case."]

random_jokes= random.randint(0,len(jokes)-1)

print(jokes[random_jokes])