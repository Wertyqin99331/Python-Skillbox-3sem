class Node:
	data = None
	next = None

	def __init__(self, value):
		self.data = value



class Queue:
	head = None
	tail = None

	def enqueue(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

	def dequeue(self):
		if self.head is None:
			return 'Queue is empty'

		result = self.head.data
		self.head = self.head.next

		if self.head is None:
			self.tail = None

		return result

	def peek(self):
		if self.head is None:
			return 'Queue is empty'

		return self.head.data