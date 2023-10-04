numbers = input('Введите числа: ').split()

used_numbers = ''
flag = True

for n in numbers:
	if n in used_numbers:
		print('true')

if flag:
	print('false')
