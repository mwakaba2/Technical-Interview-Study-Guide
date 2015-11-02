'''You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.'''

'''
@author: Mariko Wakabayashi
'''

from nose.tools import assert_equal

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(A, B):
	a_head = A
	b_head = B
	rem = 0

	if a_head and b_head:
	    sumNum = a_head.val + b_head.val
	    if sumNum > 9:
	        sumNum -= 10
	        rem = 1
	    curr = ListNode(sumNum)
	    sol = curr
	elif a_head.val: 
	    return a_head
	else:
	    return b_head
	    
	a_head = a_head.next
	b_head = b_head.next

	while a_head or b_head:
	    if a_head and b_head:
	        sumNum = a_head.val + b_head.val
	        if rem > 0 :
	            sumNum += rem
	            rem = 0
	        if sumNum > 9:
	            sumNum -= 10
	            rem = 1
	        a_head = a_head.next
	        b_head = b_head.next
	    elif a_head:
	        sumNum = a_head.val
	        if rem > 0:
	            sumNum += rem
	            rem = 0
	        if sumNum > 9:
	            sumNum -= 10
	            rem = 1
	        a_head = a_head.next
	    else:
	        sumNum = b_head.val
	        if rem > 0:
	            sumNum += rem
	            rem = 0
	        if sumNum > 9:
	            sumNum -= 10
	            rem = 1
	        b_head = b_head.next
	            
	    newNode = ListNode(sumNum)
	    curr.next = newNode
	    curr = curr.next    
	if rem > 0:
	    newNode = ListNode(rem)
	    curr.next = newNode
	return sol


def improvedAddTwoNumbers(A, B):
	a, b = A, B
	head = ListNode(0)
	cur_sum = head
	while a != None or b != None or cur_sum.val > 9:
	    carry = cur_sum.val / 10
	    cur_sum.val %= 10
	    a_val = 0 if a == None else a.val
	    b_val = 0 if b == None else b.val
	    next_val = a_val + b_val + carry
	    cur_sum.next = ListNode(next_val)
	    cur_sum = cur_sum.next
	    a = None if a == None else a.next
	    b = None if b == None else b.next
	return head.next

if __name__ == '__main__':
		A = ListNode(1)
		A.next = ListNode(1)
		B = ListNode(9)
		B.next = ListNode(9)
		answer = improvedAddTwoNumbers(A, B)
		if assert_equal(answer.val, 0) == None:
			print("Success! 1")
		if assert_equal(answer.next.val, 1) == None:
			print("Success! 2")
		if assert_equal(answer.next.next.val, 1) == None:
			print("Success! 3")