multiplesSum = 0
for i in range(3, 1000, 3):
	multiplesSum += i
for i in range(5, 1000, 5):
	multiplesSum += i
for i in range(15, 1000, 15):
	multiplesSum -= i
print(multiplesSum)