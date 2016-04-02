'''
Problem: rotate n elements to the right by k steps in an array
input: array, n, k
output: array

example: n = 4, number of elements
 k = 3, steps to move to the right
  [1, 2, 3, 4] --> [2, 3, 4, 1]
  [4, 2, 3, 1] --> [2, 4, 3, 1] --> [2, 3, 4, 1]
  k = 2 [1, 2, 3, 4] --> [3, 2, 1, 4] --> [3, 4, 1, 2]
  can you stop midway?

1. create a new list and input the numbers in the right position
	issue --> extra space
	time --> O(n)
	space --> O(n)

2. bubble sort
	issue --> O(n*k)

3. Can we do better? O(n) time O(1) space
	[1, 2, 3, 4, 5 ,6] k = 2
	[4, 3, 2, 1, 5, 6]
	[4, 3, 2, 1, 6, 5]
	[5, 6, 1, 2, 3, 4]

'''
from nose.tools import eq_

def rotateArray1(arr, k):
	n = len(arr)
	result = [0]*n
	if k > n:
		k = k % n
	for i in range(n):
		#swap values
		newIdx = (i+k) % n
		result[newIdx] = arr[i]
	return result

def rotateArray2(arr, k):
	#bubble sort
	n = len(arr)

	for i in range(k):
		for j in range(n-1, 0, -1):
			arr[j], arr[j-1] = arr[j-1], arr[j]

	return arr

def rotateArray3(arr, k):
	split = len(arr) - k

	reverse(arr, 0, split-1)
	reverse(arr, split, len(arr)-1)
	reverse(arr, 0, len(arr)-1)

	return arr
	
def reverse(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1
	return arr



lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
lst3 = [1, 2, 3, 4, 5, 6, 7, 8]

eq_([7, 8, 1, 2, 3, 4, 5, 6], rotateArray3(lst1, 2))
eq_([6, 7, 8, 1, 2, 3, 4, 5], rotateArray3(lst2, 3))
eq_([5, 6, 7, 8, 1, 2, 3, 4], rotateArray3(lst3, 4))




