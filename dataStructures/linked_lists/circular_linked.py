class Node:
	# constructor
	def __init__(self, data):
		self.data = data
		self.next = None

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self, next):
		self.next = next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next != None

class Circular:
	def __init__(self, node):
		self.head = node

	def detectCycle(self):
		if self.head == None or self.head.next == None:
			return None

		slow = self.head.next
		fast = slow.next
		while slow != fast:
			slow = slow.next

			try:
				fast = fast.next.next
			except AttributeError:
				return None
		
		slow = self.head
		while slow != fast:
			slow = slow.next
			fast = fast.next

		return slow
		
