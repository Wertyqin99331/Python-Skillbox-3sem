s = input('Введите строку: ')

zero_count = 0
one_count = 0

for ch in s:
	if ch == '0':
		zero_count += 1
	else:
		one_count += 1

print('yes' if zero_count == one_count else 'no')
