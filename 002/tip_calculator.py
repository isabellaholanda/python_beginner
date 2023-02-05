print('Welcome to the tip calculator.')
bill = float(input('What was the total of the bill? $'))
percentage_calc = int(
    input('What percentage tip would you like to give: 10, 12 or 15? '))
num_of_people = int(input('How many people to split the bill? '))

percentage = percentage_calc / 100

total = (bill + bill * percentage) / num_of_people

print(f'Each person should pay: ${round(total, 2)}')
