s = input('Введите строку: ')

result = ''

for i in range(0, len(s)):
	if i == len(s) - 1 or s[i + 1] == ' ':
		result += s[i]

print(result)
