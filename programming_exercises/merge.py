

def merge(A, B, lastA, lastB):
	indexA = lastA  - 1
	indexB = lastB - 1
	indexMerged = lastB + lastA -1

	while indexB >= 0:
		if indexA >= 0 and A[indexA] > B[indexB]:
			A[indexMerged] = A[indexA]
			indexA -=1
		else: 
			A[indexMerged] = B[indexB]
			indexB -=1
		indexMerged -=1
	return A

if __name__ == "__main__":
	A = [1,5,7,9,0,0,0,0]
	B = [2, 3, 4, 6]
	lastA = len(A) - len(B)
	lastB = len(B)
	print(merge(A, B, lastA, lastB))