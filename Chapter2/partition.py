#Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x (see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
#Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5)
#Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(linklist, x):
	current = linklist
	pre = None
	post = None
	count = 0
	while current:
		if currentdis
		.data != x:
			if current.data < x:
				if !post:
					post = linkedList(current.data)
				else:
					post.add(current.data)
			elif:
				if !pre:
					pre = linkedList(current.data)
				else:
					pre.add(current.data)
			if current.data = x:
				count += 1
		current = current.next
	current = pre.head()
	while current:
		current = current.next
	while count > 0 and if current:
		current.add(Node(x))
		current = current.next
		count -= 1
	current.next = post.head()
	return pre