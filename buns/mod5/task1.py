class Node:
	data = None
	next = None

	def __init__(self, data):
		self.data = data


class Stack:
	head = None

	def push(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def pop(self):
		if self.head is None:
			return "Stack is empty"

		item = self.head.data
		self.head = self.head.next

		return item

	def peek(self):
		if self.head is None:
			return 'Stack is empty'

		return self.head.data
