def appendFront(x, L):
	return [x+element for element in L]

def bitString(n):
	if n == 0: return []
	if n == 1: return ["0", "1"]
	else:
		return (appendFront("0", bitString(n-1)) + appendFront("1", bitString(n-1)))

def rangeToList(k):
	result = []
	for i in range(0, k):
		result.append(str(i))
	return result

def baseKString(n,k):
	if n == 0: return []
	if n == 1: return rangeToList(k)
	return [digit+bitString for digit in baseKString(1, k)
							for bitString in baseKString(n-1, k)]

print(bitString(4))
print(baseKString(3, 4))