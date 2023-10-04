phone = input('Введите номер телефона: ')

skip_symbols = ' ()-'

result = ''

for ch in phone:
	if ch not in skip_symbols:
		result += ch

print(result)
