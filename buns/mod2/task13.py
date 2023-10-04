code = input('Введите штрих-код: ')

even_sum = 0
odd_sum = 0

for i in range(0, len(code)):
	if (i + 1) % 2 == 0:
		even_sum += int(code[i])
	else:
		odd_sum += int(code[i])

print('true' if (odd_sum + even_sum * 3) % 10 == 0 else 'false')
