def findtext():
	with open("p059_cipher.txt", "r") as f:
		numbers = f.read().split(",")
	numbers = list(map(int, numbers))
	txt = ""
	for number in numbers:
		txt += chr(number)
	for i in range(ord('a'), ord('z')+1):
		for j in range(ord('b'), ord('z')+1):
			for k in range(ord('c'), ord('z')+1):
				cpy = list(txt)
				passwd = i
				for l in range(len(cpy)):
					#print(passwd)
					cpy[l] = chr(ord(cpy[l]) ^ passwd)
					if passwd == i: passwd = j
					elif passwd == j: passwd = k
					elif passwd == k: passwd = i
				ans = "".join(cpy)
				if "and" in ans and " " in ans and "the" in ans and "of" in ans and "not" in ans:
					return ans

txt = findtext()
txt = list(txt)
txt = list(map(ord, txt))
print(sum(txt))