def Pythagorean_triplet():
	for i in range(1, 1000):
		for j in range(i+1, 1001-i-1):
			k = (i**2 + j**2)**0.5
			if int(k)**2 != k**2:
				continue
			if i + j + k == 1000:
				return i*j*int(k)

print(Pythagorean_triplet())