class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class linkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		i = 0
		while current:
			i += 1
			current = current.get_next()
		return i

	def search(self,data):
		current = self.head
		while current.get_data() != data:
			current = current.get_next()
		if current is None:
			return False
		return current

	def delete(self, data):
		current = self.head
		previous = None
		while current.get_data() != data:
			current = current.get_next()
			previous = current
		if current is None:
			return False
		if previous is None:
			self.head = current.get_next()
		else
			previous.set_next(current.get_next())