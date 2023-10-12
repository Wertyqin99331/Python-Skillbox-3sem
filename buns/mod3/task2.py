a = int(input('Введите число: '))

assert a > 0, 'Неверный код'
print(bin(a)[2::], oct(a)[2::], hex(a)[2::])