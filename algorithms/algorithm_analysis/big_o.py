'''
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. O(n2). 
The second function should be linear O(n)
'''
from nose.tools import assert_equal
import time
from random import randrange

def quadratic_min(lst):
	overall_min = lst[0]
	for i in lst:
		issmallest = True
		for j in lst:
			if i > j:
				issmallest = False
		if issmallest:
			overall_min = i
	return overall_min

def linear_min(lst):
	min_num = 100
	
	for i in lst:
		if i < min_num:
			min_num = i

	return min_num


if __name__ == '__main__':
	lst = [2,3,5,6,7,7,4,9,10]
	print("Test 1 : ")
	if assert_equal(quadratic_min(lst), 2) == None:
		print("Success!")
	else:
		print("Fail!")
	print("Test 2 : ")
	if assert_equal(linear_min(lst), 2) == None:
		print("Success!")
	else:
		print("Fail!")

	for listSize in range(1000, 10001, 1000):
		alist = [randrange(100000) for x in range(listSize)]
		start = time.time()
		print(quadratic_min(alist))
		end = time.time()
		start2 = time.time()
		print(linear_min(alist))
		end2 = time.time()
		print("Quadratic find min:\nsize: %d time: %f" % (listSize, end-start))
		print("Linear find min:\nsize: %d time: %f" % (listSize, end2-start2))