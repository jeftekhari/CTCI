def p_permuation(word):
	dick = {}
	for i in word.replace(" ", "").lower():
		if i in dick:
			dick[i] += 1
		else:
			dick[i] = 1
	odds = 0
	for k in dick:
		if dick[k]%2 == 1:
			odds += 1
	return (odds<2)

print(p_permuation("Tact Coa"))
print(p_permuation("lkajsdflkaj"))