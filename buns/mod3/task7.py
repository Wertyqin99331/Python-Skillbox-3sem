numbers = input('Input some numbers: ').split(' ')
print('yes' if len(numbers) == len(set(numbers)) else 'no')