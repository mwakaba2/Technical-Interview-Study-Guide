'''
QuickSort
1. pick an element, called the pivot from the array
2. Partitioning: Reorder the array in a way that all
   elements with value less than the pivot come before the pivot,
   while all elemenst with values greater than the pivot come after it. 
   After partitioning, the pivot is in the right position. Partition operation
3. Recursively apply the above steps to the sub-arrays of elements with smaller
   values and seperately to the sub array of elements with greater values
'''


def QuickSort(A, low, high):
	if low < high:
		pivot = Partition(A, low, high)
		QuickSort(A, low, pivot-1)
		QuickSort(A, pivot+1, high)

def Partition(A, low, high):
	pivot = low
	A[pivot], A[high] = A[high], A[pivot]
	for i in range(low, high):
		if A[i] <= A[high]:
			A[i], A[low] = A[low], A[i]	
			low += 1

	A[low], A[high] = A[high], A[low]
	return low

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
QuickSort(A, 0, len(A)-1)
print(A) 