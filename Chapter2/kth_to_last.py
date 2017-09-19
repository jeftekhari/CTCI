#Implement an algorithm to find the kth to last element of a singly linked list.
#This is a bad example, because it uses a doubly linked list.

def kth_to_last(linklist, k):
	current = linklist
	while current != None:
		current = current.next
	while k > 0:
		current = current.previous
		k -= 1
	return current