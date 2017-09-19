def link_intersection(list1, list2):
	#Will have a runner and a walker. fast slow moving variables throught the lists
	#this is a bad example, time complexity is awful
	while list1:
		while list2:
			if list1 == list2:
				return True
			list2 = list2.next
		list1 = list1.next
	return False