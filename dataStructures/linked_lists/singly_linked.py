
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

class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.length = 0

	'''
	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
	def listLength(self):
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.next

		return count

	'''
	Time Complexity: O(1)
	Space Complexity: O(1)
	'''
	def insertAtBeginning(self, data):
		newNode = Node(data)
		
		if self.listLength() == 0:
			self.head = newNode
		else:
			newNode.setNext(self.head)
			self.head = newNode

		self.length += 1

	'''
	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
	def insertAtEnd(self,data):
		newNode = Node(data)

		current = self.head
		while current.getNext() != None:
			current = current.getNext()
		
		current.setNext(newNode)
		self.length += 1

	'''
	Time Complexity: O(n)
	Space Complexity: O(1) for creating one temporary variable
	'''
	def insertAtPos(self, pos, data):
		if pos > self.length or pos < 0:
			return None
		else:
			if pos == 0:
				self.insertAtBeginning(data)
			elif pos == self.length:
				self.insertAtEnd(data)
			else:
				newNode = Node(data)
				count = 0
				current = self.head

				while count < pos - 1:
					count += 1
					current = current.getNext()

				newNode.setNext(current.getNext())
				current.setNext(newNode)
				self.length += 1
		
	'''
	Time Complexity: O(1)
	Space Complexity: O(1)
	'''
	def deleteFromBeginning(self):
		if self.length == 0:
			print "This list is empty"
		else:
			self.head = self.head.getNext()
			self.length -=1
	'''
	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
	def deleteLast(self):
		if self.length == 0:
			print "The list is empty"
		else:
			current = self.head
			previous = self.head

			while current.getNext() != None:
				previous = current
				current = current.getNext()

			previous.setNext() = None
			self.length -= 1

	'''
	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
	def deleteWithNode(self, node):
		if self.length == 0:
			raise ValueError("List is empty")
		else:
			current = self.head
			previous = None
			found = False

			while not found:
				if current == node:
					found = True
				elif current is None:
					raise ValueError("Node not in linked list")
				else:
					previous = current
					current = current.getNext()

			if previous = None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())
			self.length -= 1

	def deleteWithValue(self, value):
		current = self.head
		previous = self.head

		while not current.getNext() != None or current.data != value:
			if current.data == value:
				previous.setNext() = current.getNext()
				self.length -= 1
				return
			else:
				previous = current
				current = current.getNext()

		print "No such value in the linked list"

	def deleteAtPosition(self, pos):
		count = 0
		current = self.head
		previous = self.head

		if pos > self.length or pos < 0:
			print "Invalid position"
		else:
			while current.getNext() != None or count < pos:
				count = count + 1
				if count == pos:
					previous.setNext() = current.getNext()
					self.length -=1
					return
				else:
					previous = current
					current = current.getNext()
		

	def clear(self):
		self.head = None


if __name__ == '__main__':
	newList = SinglyLinkedList()
	
	for i in range(10, 0, -1):
		newList.insertAtBeginning(i)

	print(newList.length)

	newList.insertAtPos(3, 100)
	print(newList.length)

