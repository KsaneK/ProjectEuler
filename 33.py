result = 1
for i in range(1, 100):
	for j in range(i + 1, 100):
		if i/10 == 0 or j%10 == 0:
			continue
		if i%11 == 0:
			continue
		digit1 = int(i/10)
		digit2 = j%10
		if i%10 == int(j/10) and i/j == digit1 / digit2:
			result *= i/j
print(round(result,5))