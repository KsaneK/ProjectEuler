for i in range(1, 10000):
	digits = []
	nextnum = False
	for j in range(1, 10):
		strnum = str(i * j)
		for dig in strnum:
			if dig in digits or dig == "0":
				nextnum = True
				break
			digits.append(dig)
		if nextnum == True:
			break
		if len(digits) == 9:
			print("".join(digits))
			break