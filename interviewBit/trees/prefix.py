'''Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov

'''

def prefix(list):
	tree = [0,{}]

	for word in list:
		node = tree
		node[0] += 1
		for char in word:
			node = node[1].setdefault(char, [0, {}])
			node[0] +=1

	prefixes = []
	for word in list:
		prefix = ""
		node = tree
		for char in word:
			if node[0] <= 1:
				prefixes.append(prefix)
				break
			prefix += char
			node = node[1][char]
		#else if a prefix is not found, use the whole word as a prefix
		else:
			prefixes.append(word)
	return prefixes




if __name__ == '__main__':
	lst = ["dog", "dove", "zebra", "dominic", "david", "duck"]
	print(prefix(lst))