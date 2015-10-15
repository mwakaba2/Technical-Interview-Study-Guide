'''Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.'''

class Solution:
	# @param x : integer
	# @param n : integer
	# @param d : integer
	# @return an integer
	'''Initial Solution: Two problems with the solution
	   1. Uses recursion but time complexity is O(x). Goal is to reduce time complexity
	   2. Overflow problem: If x is large enough, multiplying x to the answer might overflow
	   '''
	def power_mod(self, x, n, d):
		if x == 0:
			return 0
		if n == 0:
			return 1
		else:
			return x*self.power_mod(x, n-1, d) % d

	def pow2(self, x, n, d):
		result = 1
		base = x % d
		while n > 0:
			if n % 2 == 1:
				result = (result * base) % d
			#One bit shifted to the right: n // 2**1
			n = n >> 1
			base = (base*base) % d
		return result % d

x = 2
n = 50
d = 10

answer = Solution.power_mod(Solution(), x, n, d)
answer1 = Solution.pow2(Solution(), x, n, d)
print(answer)
print(answer1)