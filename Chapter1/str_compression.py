def str_compression(myString):
	#trying to implement dictionary but couldnt due to same key values
	#
	# dicty = {}
	# newStr = ""
	# for i in myString:
	# 	if i in dicty:
	# 		dicty[i] += 1
	# 	else:
	# 		dicty[i] = 1
	# 	print(dicty)
	# for k in dicty:
	# 	if dicty[k] > 0:
	# 		newStr = newStr + k
	# 		newStr = newStr + str(dicty[k])
	# if len(newStr) >= len(myString):
	# 	return myString
	# return newStr

	#using a counter and editing the string
	newStr = myString[0]
	count = 1
	for i in range(1,len(myString)):
		if myString[i] == myString[i - 1]:
			count += 1
		else:
			newStr += str(count) + myString[i]
			count = 1
	newStr += str(count)
	if len(newStr) > len(myString):
		return myString
	return newStr

print(str_compression("aabcccccaaa"))
print(str_compression("abccd"))