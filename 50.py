def isPrime(N):
	if N == 2:
		return True
	for i in range(2, int(N**0.5)+1):
		if N % i == 0:
			return False
	return True

i = 1
primes_sum = 0
primes = []
while primes_sum < 1000000:
	i+=1
	if isPrime(i):
		primes_sum += i
		primes.append(i)
		
primes_sum -= primes[-1]

answer = (0,0)
for i in range(10):
	tmp_sum = primes_sum
	tmp_len = len(primes)
	j = 0
	while not isPrime(tmp_sum) or tmp_sum > 1000000:
		tmp_sum -= primes[j]
		tmp_len -= 1
		j+=1
	if tmp_len > answer[1]:
		answer = (tmp_sum, tmp_len)
print(answer)