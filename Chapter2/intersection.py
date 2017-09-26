def link_intersection(list1, list2):
	#Will have a runner and a walker. fast slow moving variables throught the lists
	#this is a bad example, time complexity is awful
	# while list1:
	# 	while list2:
	# 		if list1 == list2:
	# 			return True
	# 		list2 = list2.next
	# 	list1 = list1.next
	# return False

	## take the length of both lists, then subtract the difference from the larger list.
	##this ensures that both lists start the same distance apart from the list.
	# order of O(n) with space complexity of O(1)
	len1 = len(list1)
	len2 = len(list2)
	length = abs(len1 - len1)
	if len1 > len2:
		list1 = list1[lenth]
	else:
		list2 = list2[length]
	while (list1 != list2):
		list1 = list1.next
		list2 = list2.next
		if list1 == list2:
			return list1
	return False
