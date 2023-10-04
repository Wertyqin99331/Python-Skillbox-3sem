import math

a = int(input('Введите длину стороны квадрата: '))

p = round(a * 4, 2)
s = round(a * a, 2)
d = round(math.sqrt(2) * a, 2)
print(p, s, d)