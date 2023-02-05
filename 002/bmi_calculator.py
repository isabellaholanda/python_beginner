'''
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Warning you should convert the result to a whole number.

Example Input
weight = 80
height = 1.75
Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
'''


height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')

bmi = float(weight) / (float(height) ** 2)
bmi_int = int(bmi)
print(bmi_int)
