	
def mergesort(lst):
	helper = [0] * len(lst)
	mergesort_helper(lst, helper, 0, len(lst)-1)

def mergesort_helper(lst, helper, low, high):
	print("Splitting start: {0}, end: {1}".format(low, high))
	if low < high:
		middle = (low + high) // 2
		mergesort_helper(lst, helper, 0, middle)
		mergesort_helper(lst, helper, middle+1, high)
		merge(lst, helper, low, middle, high)
		print("Merging ",helper)
def merge(lst, helper, low, middle, high):
	for i in range(low, high+1):
		helper[i] = lst[i]

	helperLeft = low
	helperRight = middle+1
	current = low

	while helperLeft <= middle and helperRight <= high:
		if helper[helperLeft] <= helper[helperRight]:
			lst[current] = helper[helperLeft]
			helperLeft +=1
		else:
			lst[current] = helper[helperRight]
			helperRight +=1
		current +=1
	
	remaining = middle - helperLeft
	for i in range(remaining+1):
		lst[current+i] = helper[helperLeft+i]
	

def mergeSort2(a_list, start=0, stop=None):
	print("Splitting {0} {1}".format(start, stop))
	if stop == None:
		stop = len(a_list)
	if stop - start > 1:
		mid = (start + stop) // 2
	
		mergeSort2(a_list,start,mid)
		mergeSort2(a_list,mid,stop)

		merge2(a_list, [], start, mid, stop)
		
def merge2(a_list, n_list, start, mid, stop):
		rightHalf = mid
		leftHalf = start
		while leftHalf < mid and rightHalf < stop:
			if a_list[leftHalf] < a_list[rightHalf]:
				n_list.append(a_list[leftHalf])
				leftHalf += 1
			else:
				n_list.append(a_list[rightHalf])
				rightHalf += 1

		while leftHalf < mid :
				n_list.append(a_list[leftHalf])
				leftHalf += 1
		
		while rightHalf < stop :
				n_list.append(a_list[rightHalf])
				rightHalf += 1
		a_list[start:stop] = n_list
		print("Merging {0}".format(n_list))


if __name__ == '__main__':
	lst1 = [0,2,5,7,9,4,6,8,1]
	mergesort(lst1)
	print lst1
	alist = [54,26,93,17,77,31,44,55,20]
	mergeSort2(alist)
	print(alist)