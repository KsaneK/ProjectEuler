def isPrime(N):
	if N == 2:
		return True
	for i in range(2, int(N**0.5)+1):
		if N % i == 0:
			return False
	return True

n = 0
i = 1
while n < 10001:
	i+=1
	if isPrime(i):
		n+=1
print(i)