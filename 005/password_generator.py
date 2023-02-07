import random
import letters_symbols_numbers

print('Welcome to the PyPassowrd Generator.')
num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))

password = []

for letter in range(num_letters):
    password.append(random.choice(letters_symbols_numbers.letters))

for symbol in range(num_symbols):
    password.append(random.choice(letters_symbols_numbers.symbols))

for number in range(num_numbers):
    password.append(random.choice(letters_symbols_numbers.numbers))

random.shuffle(password)
final_password = ''

for word in password:
    final_password += word

print(f'Here is your password: {final_password}')
