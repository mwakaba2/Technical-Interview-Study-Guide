'''
Given a sorted array of integers, find the starting and ending position of a given target value.
Runtime --> logn
If the target is not found in the array, return [-1, -1].

Example:
Given [5, 7, 7, 8, 8, 10]
and target value 8,
return [3, 4].
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers

	def searchRange(self, A, B):
		low = 0
		high = len(A)-1
		indices = [-1, -1]

		while low < high:
			mid = (low+high) / 2

			if A[mid] == B:
				high = mid
			elif A[mid] < B:
				low = mid + 1
			else: 
				high = mid - 1

		if A[low] != B:
			return indices

		indices[0] = low
		high = len(A) - 1

		while low < high:
			mid = (low+high+1) / 2
			if A[mid] == B:
				low = mid
			else:
				high = mid - 1

		indices[1] = low
		return indices

A = [5, 7, 7, 8, 8, 8, 8, 8]
B = 8
print('A: '+str(A))
print('B: '+str(B))
print(Solution.searchRange(Solution(),A,B))
