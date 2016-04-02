'''
Problem: evaluate the value of an arithmetic expression in reverse polish notation


["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

1. Create a stack 
	a. remove all elements and evaluate once you get an operator push it back
	b. should be left with one value at the end
	c. Time O(n)
	d. Space O(n)

'''
from nose.tools import eq_

def calculate(op, first, second):
	if op == "+":
		return first + second
	elif op == "-":
		return first - second
	elif op == "/":
		return first / second
	elif op == "*":
		return first * second
	else:
		return -1

def evaluate(expression):
	stack = []

	for exp in expression:
		if exp.isdigit():
			stack.append(exp)
		else:
			if len(stack) >= 2:
				second = stack.pop()
				first = stack.pop()
				value = calculate(exp, int(first), int(second))
				stack.append(value)
			else:
				return -1

	return stack.pop()




if eq_(9, evaluate(["2", "1", "+", "3", "*"])) == None:
	print("Passed Test One!")

if eq_(6, evaluate(["4", "13", "5", "/", "+"])) == None:
	print("Passed Test Two!")

print("Done!")