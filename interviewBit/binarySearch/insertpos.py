'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 - 2
[1,3,5,6], 2 - 1
[1,3,5,6], 7 - 4
[1,3,5,6], 0 - 0


The pattern you can see here is that 
-- when the number is in between some numbers in the list, we give the index of the right end
-- when the number does not exist and is the lowest then index 0
-- when the number does not exist and is the highest then provide the last index+1
'''
from nose.tools import assert_equal

class Solution:

	def searchInsert(self, A, B):
		low = 0
		high = len(A)-1
		index = 0

		while low <= high:
			mid = (low+high) / 2
			if A[mid] == B:
				return mid
			else:
				if A[mid] > B:
					high = mid - 1
					index = mid
				else:
					low = mid + 1
					index = low
		
		return index

A = [1, 3, 5, 6]
assert_equal(Solution.searchInsert(Solution(), A, 5), 2)
assert_equal(Solution.searchInsert(Solution(), A, 2), 1)
assert_equal(Solution.searchInsert(Solution(), A, 7), 4)
assert_equal(Solution.searchInsert(Solution(), A, 0), 0)



