def prime_checker(number):
    num_list = []
    for num in range(1, number + 1):
        if number % num == 0:
            num_list.append(num)
    if len(num_list) == 2 and 1 in num_list and number in num_list:
        print('It\'s a prime number')
    else:
        print('It\'s not a prime number')


n = int(input('Check this number: '))
prime_checker(number=n)
