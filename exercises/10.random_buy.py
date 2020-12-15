
#The goal is to not use random.choice as it is easy to use.
#Instead, trying to use len & random randit.

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list = len(names)
choice = random.randint(0, list -1)
person = names[choice]
print(f"{person} is going to buy the meal")
