n = int(input('Input matrix size: '))

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if j != n:
			print(j, end=', ')
		else:
			print(j)

print()

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if j != n:
			print(i, end=', ')
		else:
			print(i)
