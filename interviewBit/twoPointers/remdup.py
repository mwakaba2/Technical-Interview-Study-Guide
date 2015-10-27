'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 


@author: Mariko Wakabayashi
'''


def removeDuplicates(A):
	i = 1
	j = 1
	n = len(A)
	while i < n and j < n:
		if A[j] == A[j-1]:
			j += 1
		else:
			A[i] = A[j] 
			i += 1
			j += 1
	print "New list looks like...: " + str(A)
	return i




if __name__ == '__main__':
	list1 = [1,2,2,2,2,2,4,5,7,7,7,7,7,7,7,8,8]
	print("New length is: "+str(removeDuplicates(list1)))
