class MinStack:

	def __init__(self):
		self.stack = []
		self.minimums = []
	# @param x, an integer
	def push(self, x):
		if len(self.stack) == 0:
			self.stack.append(x)
			self.minimums.append(x)
		else:
			self.stack.append(x)
			if x < self.minimums[-1]:
				self.minimums.append(x)
			else:
				self.minimums.append(self.minimums[-1])

	# @return nothing
	def pop(self):
		if len(self.stack) != 0:
			popped = self.stack.pop()
			self.minimums.pop()
		return popped

	# @return an integer
	def top(self):
		if len(self.stack) == 0:
			return -1
		else:
			return self.stack[-1]

	# @return an integer
	def getMin(self):
		try:
			return self.minimums[-1]
		except IndexError as ie:
			return "no elements in the stack"
			


minimum_stack = MinStack()
print(minimum_stack.getMin())
minimum_stack.push(5)
minimum_stack.push(6)
minimum_stack.push(4)
minimum_stack.push(1)
minimum_stack.push(7)
minimum_stack.push(2)
print(minimum_stack.stack)
print(minimum_stack.minimums)
print(minimum_stack.pop())
