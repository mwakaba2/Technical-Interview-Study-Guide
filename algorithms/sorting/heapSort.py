'''
heapSort

1. build a max heap from a list of unsorted numbers
2. Swap the first element of the list with the final element.
   Decrease the considered range of the list by one
3. Call percolateDown to position the new first element to the appropriate index in the heap
4. repeat until left with one element
'''

def heapSort(A):
	length = len(A) - 1
	leastParent = length / 2
	for i in range(leastParent, -1, -1):
		percolateDown(A, i, length)

	for i in range(length, 0, -1):
		if A[0] > A[i]:
			A[0], A[i] = A[i], A[0]
			percolateDown(A, 0, i-1)

	return A


def percolateDown(A, first, last):
	largest = 2 * first + 1
	while largest <= last:
		if (largest < last) and (A[largest] < A[largest+1]):
			largest += 1
		if A[largest] > A[first]:
			A[largest], A[first] = A[first], A[largest]
			first = largest
			largest = 2 * first + 1
		else:
			return


if __name__ == '__main__':
	lst = [2, 6, 3, 87, 4, 3, 123, 9, 6, 8]
	print(heapSort(lst))