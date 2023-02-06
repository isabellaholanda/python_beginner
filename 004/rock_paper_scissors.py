from random import randint
import icons

print('Welcome to Rock, Paper and Scissors!')
player_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper and 2 \
for Scissors.\n'))

valid_numbers = [0, 1, 2]

if player_choice not in valid_numbers:
    print('Not a valid number. Game Over.')
else:
    options = [icons.rock, icons.paper, icons.scissors]

    computer_choice = randint(0, 2)

    print('Player Choice:\n', options[player_choice])
    print('Computer Choice:\n', options[computer_choice])

    if player_choice == computer_choice:
        print('It is a tie')
    elif player_choice == 0 and computer_choice != 2:
        print('You Lose. Game Over.')
    elif player_choice == 1 and computer_choice != 0:
        print('You Lose. Game Over.')
    elif player_choice == 2 and computer_choice != 1:
        print('You Lose. Game Over.')
    else:
        print('You Won.')
