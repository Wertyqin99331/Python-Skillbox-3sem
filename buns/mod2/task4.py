a = int(input('Введите число в 10-чной системе: '))

assert a > 0, 'Message'

print(bin(a)[2::], oct(a)[2::], hex(a)[2::])