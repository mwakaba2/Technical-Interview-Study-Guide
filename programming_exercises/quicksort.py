def quickSort(alist):
  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
  if first<last:
    splitpoint = partition(alist,first,last)

    quickSortHelper(alist,first,splitpoint-1)
    quickSortHelper(alist,splitpoint+1,last)

def partition(A,first,last):
  pivotvalue = first
  A[pivotvalue], A[last] = A[last], A[pivotvalue]
  for i in range(first, last):
    if A[i] <= A[last]:
      A[i], A[first] = A[first], A[i]
      first +=1
  A[first], A[last] = A[last], A[first]
  return first

   # leftmark = first+1
   # rightmark = last

   # done = False
   # while not done:

   #     while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
   #         leftmark = leftmark + 1

   #     while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
   #         rightmark = rightmark -1

   #     if rightmark < leftmark:
   #         done = True
   #     else:
   #         temp = alist[leftmark]
   #         alist[leftmark] = alist[rightmark]
   #         alist[rightmark] = temp

   # temp = alist[first]
   # alist[first] = alist[rightmark]
   # alist[rightmark] = temp


   # return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
