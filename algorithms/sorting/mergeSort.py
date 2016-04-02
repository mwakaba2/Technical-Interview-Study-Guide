'''
1. Divide the unsorted list into n sublists, 
   each containing 1 element (a list of 1 element is considered sorted)
2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 
   1 sublist remaining. This will be the sorted list. 
'''


def MergeSort(A):
	if len(A) > 1:
		mid = len(A) // 2
		leftHalf = A[:mid]
		rightHalf = A[mid:]
		MergeSort(leftHalf)
		MergeSort(rightHalf)
		i = j = k = 0
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				A[k] = leftHalf[i]
				i = i + 1
			else:
				A[k] = rightHalf[j]
				j = j + 1
			k = k + 1

		while i<len(leftHalf):
			A[k] = leftHalf[i]
			i = i + 1
			k = k + 1

		while j<len(rightHalf):
			A[k] = rightHalf[j]
			j = j + 1
			k = k + 1

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
MergeSort(A)
print(A) 
