



def reverse(word):
	reversed_words = word.split()[::-1]
	return " ".join(reversed_words)
 
if __name__ == '__main__':
	word = "My name is Mariko"
	print("The reverse word for {0} is: {1}".format(word, reverse(word)))
