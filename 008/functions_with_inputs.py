def greet(name):
    print(f'Hello {name}')
    print(f'How are you {name}?')
    print('It is a lovely day today.')


greet('Isabella')


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'How is it like in {location}?')


greet_with('Isabella', 'Fortaleza')
greet_with(location='Fortaleza', name='Isabella')
