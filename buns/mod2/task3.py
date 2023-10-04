a, b, c = map(int, input('Введите 3 числа: ').split(' '))

if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)