vowels_letters = 'аеёиоуыэюя'
consonants_letters = 'бвгджзйклмнпрстфхцчшщьъ'

s = input('Введите вашу строку: ')

vowels_count = 0
consonants_count = 0

for ch in s:
	if ch in vowels_letters:
		vowels_count += 1
	elif ch in consonants_letters:
		consonants_count += 1

print(vowels_count, consonants_count)
