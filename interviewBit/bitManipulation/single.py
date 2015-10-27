'''Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3

@author: Mariko Wakabayashi

explanation: XOR is great for figuring out if two numbers are equal or not. 
If they are equal, XOR cancels it out and give you 0.
'''


def singleNumber(A):
	ret = 0
	for i in A:
		ret = ret ^ i
	return ret


if __name__ == '__main__':
	list1 = [1,1,2,2,4,5,4,5,6]
	print(singleNumber(list1))