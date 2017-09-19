
## Other Data Structures ##
def is_unique(word):
	dick = {}
	for i in word:
		if i in dick:
			print("no")
			return 0
		else:	
			dick[i] = 1
	print("yes")
	return 1

## No Other Data Structures
def is_unique1(word):
	for i in range(0, len(word)):
		for k in range(i + 1, len(word)):
			if word[i] is word[k]:
				print("no")
				return 0
	print("yes")
	return 1

is_unique1("abcde")
is_unique1("aabcde")