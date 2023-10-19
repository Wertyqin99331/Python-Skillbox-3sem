def pow(num, exp):
	if exp == 1:
		return num
	if num % 2 == 0:
		return (num * num)**pow(num, exp // 2)
	return num * pow(num, exp - 1)


num = int(input('Input your num: '))
print(pow(num, 3))
