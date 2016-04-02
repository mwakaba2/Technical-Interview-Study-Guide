def reverse(str):
	str = list(str)
	n = len(str)
	if n % 2 == 0:
		mid = ((n-1)//2)+1
	else:
		mid = (n-1) // 2
		
	for i in range(mid):
		str[i], str[n-i-1] = str[n-i-1], str[i]

	return ''.join(str)


def fastReverse(str):
	return str[::-1]


def mostPythonicReverse(str):
	return ''.join(reversed(str))





print(reverse("hello world"))
print(fastReverse("hello world"))
print(mostPythonicReverse("hello world"))