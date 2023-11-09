class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, val):
		new_node = Node(val)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node

	def get(self, index):
		current = self.head
		for _ in range(index):
			if current is None:
				raise IndexError("Index out of range")
			current = current.next
		if current is None:
			raise IndexError("Index out of range")
		return current.data

	def remove(self, index):
		if index == 0:
			if self.head:
				self.head = self.head.next
			else:
				raise IndexError("Index out of range")
		else:
			current = self.head
			for _ in range(index - 1):
				if current is None or current.next is None:
					raise IndexError("Index out of range")
				current = current.next
			if current.next:
				current.next = current.next.next
			else:
				raise IndexError("Index out of range")

	def insert(self, index, val):
		new_node = Node(val)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
		else:
			current = self.head
			for _ in range(index - 1):
				if current is None:
					raise IndexError("Index out of range")
				current = current.next
			if current:
				new_node.next = current.next
				current.next = new_node
			else:
				raise IndexError("Index out of range")

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next
