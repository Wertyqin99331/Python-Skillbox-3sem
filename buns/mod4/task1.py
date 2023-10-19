nums = list(map(int, input('Input your numbers: ').split(' ')))

print('Все числа равны' if len(set(nums)) == 1 else 'Все числа разные' if len(set(nums)) == len(nums) else 'Есть равные и не равные числа')
