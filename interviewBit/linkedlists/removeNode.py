
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

def removeNode(start, target):
	curr = start
	while curr != None:
		if curr.val == target:
			if curr.prev != None:
				curr.prev.next = curr.next
			if curr.next != None:
				curr.next.prev = curr.prev
			print("removing {0}".format(curr.val))
			break
		curr = curr.next

			
if __name__ == "__main__":
	head = ListNode(4)
	head.prev = None
	head.next = ListNode(20)
	head.next.prev = head
	head.next.next = ListNode(4)
	head.next.next.prev = head.next
	print(removeNode(head, 4))