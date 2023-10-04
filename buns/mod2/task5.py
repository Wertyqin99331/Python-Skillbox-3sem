import string

print(string.ascii_lowercase)

ch, n = input('Введите символ латинского алфавита и число смещения: ').split()
n = int(n)

print(chr(97 + ((ord(ch) - 97) + n) % 26))
