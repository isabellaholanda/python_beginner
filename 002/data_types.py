'''
Instructions
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Example Input
39
Example Output
3 + 9 = 12
12
'''

two_digit_num = (input('Type a two digit number: '))

num_1 = int(two_digit_num[0])
num_2 = int(two_digit_num[1])

sum_num = num_1 + num_2

print(sum_num)
