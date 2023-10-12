phone_number = input('Input your phone number: ')
print(''.join([ch for ch in phone_number if ch not in ['-', '(', ')', ' ']]))