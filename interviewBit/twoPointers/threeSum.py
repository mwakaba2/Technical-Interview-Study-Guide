#!/usr/bin/env python

'''
@author: Mariko Wakabayashi
'''

'''Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)'''

import sys

def threeSumClosest(array, target):
	array.sort()
	diff = sys.maxint
	solution = 0
	if len(array) < 3:
		return 0

	for i in xrange(len(array)-2):
		left = i+1
		right = len(array)-1
		while left < right:
			sum = array[i]+array[left]+array[right]
			if abs(target - sum) < diff:
				diff = abs(target - sum)
				solution = sum
			elif sum > target:
				right -=1
			else:
				left +=1
	return solution



if __name__ == '__main__':
    array = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(array, target))