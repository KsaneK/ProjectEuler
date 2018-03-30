# [
# 	65, 64, 63, 62, 61, 60, 59, 58, 57,
# 	66, 37, 36, 35, 34, 33, 32, 31, 56,
# 	67, 38, 17, 16, 15, 14, 13, 30, 55,
# 	68, 39, 18,  5,  4,  3, 12, 29, 54,
# 	69, 40, 19,  6,  1,  2, 11, 28, 53,
# 	70, 41, 20,  7,  8,  9, 10, 27, 52,
# 	71, 42, 21, 22, 23, 24, 25, 26, 51,
# 	72, 43, 44, 45, 46, 47, 48, 49, 50,
# 	73, 74, 75, 76, 77, 78, 79, 80, 81
# ]
def isPrime(N):
	if N == 2:
		return True
	for i in range(2, int(N**0.5)+1):
		if N % i == 0:
			return False
	return True

diffs = [2, 4, 6, 8]
corners = [3, 5, 7, 9]
primes = 3
numbers = 5
while primes / numbers > 0.1:
	numbers += 4
	diffs = [x+8 for x in diffs]
	corners = [corners[i] + diffs[i] for i in range(4)]
	for num in corners:
		if isPrime(num):
			primes+=1

print("Primes: ", primes)
print("Numbers: ", numbers)
print("Ratio: ", primes/numbers)
print("Length: ", end='')
print(int(numbers/4 * 2 + 1))
