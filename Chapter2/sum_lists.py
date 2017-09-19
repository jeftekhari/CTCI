
#You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
#Output: 2 -> 1 -> 9.That is, 912.

def sum_lists(list1, list2):
	result = ""
	result2 = ""
	while list1.next or list2.next:
		if list1.next:
			list1 = list1.next
		if list2.next:
			list2 = list2.next
	while list1.prev or list2.prev:
		if list1.prev:
			result.append(list1.data)
			list1 = list1.prev
		if list2.prev:
			result2.append(list2.data)
			list2 = list2.prev
	return result += result2