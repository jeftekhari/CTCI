def check_permutation(str1, str2):
	arr = {}
	for i in str1:
		if i in arr:
			arr[i] += 1
		else:
			arr[i] = 1
	print(dick)
	for k in str2:
		if k in arr:
			arr[k] -= 1
			if arr[k] == 0:
				del arr[k]
		else:
			print("no")
			return 0
	if arr == {}:
		print("yes")
		return 1
	print("no")
	return 0

check_permutation("abcd", "bcda")
check_permutation("abcd", "abd")