#strings.py
#saved the information into a variable
hero="Super Man"
#replacing spaces with ^
hero2=hero.replace("","^").strip("^")
hero2=hero2.replace("^ ^"," ").upper()
print(hero2) 
