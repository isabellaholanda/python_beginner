print('Welcome to')
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')

print('Your mission is to find the treasure.')

choice = input('You are at a cross road. Where do you want to go? \
Typy "left" or "right"? ').lower()

if choice == 'left':
    choice = input(
        'You come to a lake. There is an island in the middle of the lake. \
Type "wait" to wait for a boat or "swim" to swim across. ').lower()
    if choice == 'wait':
        choice = input(
            'You arrive at the island unharmed. There is a house with 3 doors.\
 One red, one yellow and one blue. Which colour do you choose? ').lower()
        if choice == 'yellow':
            print('You found the treasure. You Win!')
        elif choice == 'red':
            print('You enter a room with beasts. Game Over.')
        elif choice == 'blue':
            print('You enter a room with crocodiles. Game Over.')
    else:
        print('You were surrounded by carnivorous fish. Game Over.')
else:
    print('You fell into a hole. Game Over.')
