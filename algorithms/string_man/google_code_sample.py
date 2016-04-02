# find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
# find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1).
# The array and the number of duplicates can be large.

from nose.tools import eq_

def find_range(lst, target):
	start, end = -1, -1
	foundFirst = False
	for i in range(len(lst)):
		if lst[i] == target:
			if not foundFirst:
				foundFirst = True
				start = i
				end = i
			else:
				end += 1
	return start, end


eq_(find_range([0,2,3,3,3,10,10], 3), (2,4))
eq_(find_range([0,2,3,3,3,10,10], 6), (-1,-1))
eq_(find_range([0,2,3,3,3,10,10], 2), (1,1))

def largestSum(lst):
	largestSum = 0
	currentSum = 0

	for i in range(len(lst)):
		currentSum += lst[i]
		if currentSum < 0:
			currentSum = 0
		if currentSum > largestSum:
			largestSum = currentSum

	return largestSum


def largestSumBinary(lst):
	

eq_(largestSum([-2, -3, 4, -1, -2, 1, 5, -3]), 7)