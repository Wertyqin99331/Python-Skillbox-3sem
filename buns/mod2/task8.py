s, ch = input('Введите строку и символ: ').split(' ')

i = 0

while i < len(s) and s[i] == ch:
	i += 1

print(i)
