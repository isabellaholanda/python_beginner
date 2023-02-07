import random
import hangman_file
import os

print(f'{hangman_file.logo}\n')

game_over = False
lives = len(hangman_file.stages) - 1

key_word = random.choice(hangman_file.game_word_list)
try_word = []

for blank in key_word:
    try_word.append('_')

print(' '.join(try_word))

while not game_over:
    player_choice = input('Guess a letter: ').lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    count = 0
    if player_choice in key_word:
        for letter in key_word:
            if letter == player_choice:
                try_word[count] = letter
            count += 1
    else:
        print(
            f'You guessed the letter "{player_choice}", that is not in \
the word. You lose a life!')
        lives -= 1

    if '_' not in try_word:
        game_over = True
        print('You Won!')
    elif lives < 1:
        game_over = True
        print('Game Over!')

    print(' '.join(try_word))
    print(hangman_file.stages[lives])
