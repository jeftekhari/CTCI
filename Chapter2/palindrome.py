def list_palindrome(list1):
	temp = list1
	while temp.next:
		temp = temp.next
	while list1.data == temp.data:
		list1 = list1.next
		temp = temp.prev
		if list1 == temp:
			return True
	return False