def isSubstring(sub, whole):
	for i in xrange(len(whole)-len(sub)+1):
		subsection = whole[i:i+len(sub)]
		print(subsection)
		if sub == subsection:
			return 1
	return 0


if __name__ == "__main__":
	sub = "bat"
	whole = "abustabat"
	print(isSubstring(sub, whole))