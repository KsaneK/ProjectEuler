def problem4():
	maxPallindrome = 0
	for i in range(999, 100, -1):
		for j in range(999, 100, -1):
			num = str(i * j)
			if num == num[::-1] and int(num) > maxPallindrome:
				maxPallindrome = int(num)
	return maxPallindrome

print(problem4())