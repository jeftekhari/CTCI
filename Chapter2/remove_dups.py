#remove dups from an unsorted linked list

def remove_dups(linklist):
	slow = linklist
	while slow != None:
		fast = slow
		while fast.next != None:
			if fast.next.data == slow.data:
				fast.next = fast.next.next
			else:
				fast = fast.next
		slow = slow.next