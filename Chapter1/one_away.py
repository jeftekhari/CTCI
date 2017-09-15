def one_away(word1, word2):
	dicty = {}
	for i in word1:
		if i in dicty:
			dicty[i] += 1
		else:
			dicty[i] = 1
	for k in word2:
		if k in dicty:
			dicty[k] -= 1
			if dicty[k] == 0:
				del dicty[k]
	if len(dicty) == 1 or len(dicty) == 0:
		return True
	return False

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))