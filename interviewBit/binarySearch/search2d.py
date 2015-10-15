'''Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem'''




class Solution:
	# @param A : list of list of integers
	# @param B : integer
	# @return an integer
	'''My Initial Solution'''
	def searchMatrix(self, A, B):
		low = 0
		high = len(A)-1
		midlist_idx = (low+high)// 2

		while low <= high:
		    if B == A[midlist_idx][0]:
		        return 1
		    elif B == A[midlist_idx][-1]:
		        return 1
		    elif B < A[midlist_idx][0]:
		        high = midlist_idx-1
		    elif B > A[midlist_idx][-1]:
		        low = midlist_idx+1
		    else:
		        return self.binarySearch(A[midlist_idx], B)
		    midlist_idx = (low+high)// 2
		return 0

	def binarySearch(self, lst, num):
		low = 0
		high = len(lst)-1
		mid = (high+low) // 2

		while low <= high:
		    if lst[mid] == num:
		        return 1
		    elif lst[mid] > num:
		        high = mid-1
		    elif lst[mid] < num:
		        low = mid + 1
		    mid = (high+low) // 2
	    
		return 0

	'''Improved Answer'''
	def searchMatrix2(self, A, B):
		m = len(A)
		if m == 0:
			return 0
		n = len(A[0])
		low = 0
		high = m*n-1

		while low <= high:
			mid = (low+high) // 2
			i = mid/n
			j = mid%n
			if A[i][j] == B:
				return 1
			elif A[i][j] < B:
				low = mid + 1
			else:
				high = mid -1
		return 0

print(
	Solution.searchMatrix(Solution(),
	[
		[1,   3,  5,  7],
		[10, 11, 16, 20],
		[23, 30, 34, 50]
	], 3)
)

print(
	Solution.searchMatrix2(Solution(),
	[
		[1,   3,  5,  7],
		[10, 11, 16, 20],
		[23, 30, 34, 50]
	], 3)
)
