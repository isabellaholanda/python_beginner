import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# random_choice = random.randint(0, len(names) - 1)
random_choice = random.choice(names)

# print(f'{names[random_choice]} is going to buy the meal today!')
print(f'{random_choice} is going to buy the meal today!')
