print('Welcome to the Love Calculator!')
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

names = name1.lower() + name2.lower()


decimal = 0
unitary = 0

decimal += names.count('t') + names.count('r') + \
    names.count('u') + decimal + names.count('e')

unitary += names.count('l') + names.count('o') + \
    names.count('v') + names.count('e')

percentage = str(decimal) + str(unitary)
percentage_int = int(percentage)

if percentage_int < 10 or percentage_int > 90:
    print(
        f'Your score is {percentage}, you go together like coke and mentos.')
elif percentage_int >= 40 and percentage_int <= 50:
    print(f'Your score is {percentage}, you are alright together.')
else:
    print(f'Your score is {percentage}.')
