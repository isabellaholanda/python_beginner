from caesar_cipher_logo import logo
from caesar_cipher_logo import alphabet

print(logo)


def caesar(plain_text, shift_amount, the_direction):
    new_word = ''
    for i in plain_text:
        if i not in alphabet:
            new_word += i
        else:
            if the_direction == 'encode':
                new_word += alphabet[alphabet.index(i) + shift_amount]
            elif the_direction == 'decode':
                new_word += alphabet[alphabet.index(i) - shift_amount]
    print(f'The {the_direction} text is: {new_word}')


its_on = True
while its_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift_amount number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    end_program = input(
        'Type "yes" if you want to go again. Otherwise type "no". ').lower()
    if end_program == 'no':
        its_on = False
        print('Good bye!')
