domain = input('Введите домен сайта: ')

result = ''

for i in range(len(domain) - 1, -1, -1):
	if domain[i] == '.':
		print(result[::-1])
		result = ''
	else:
		result += domain[i]
		if i == 0:
			print(result[::-1])
