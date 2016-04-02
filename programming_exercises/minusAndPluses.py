'''
input: string 
output: list of possible moves

for example: "++--++--"
output: ["++++++--", "++--++++"]

'''

def possibleMoves(move):
	global moves
	moves = []
	return possibleM(move, 0)


def possibleM(move, start):
	global moves
	if start >= len(move)-1:
		return moves
	if move[start] == move[start+1] and move[start] == "-":
		temp = list(move)
		temp[start:start+2] = "++"
		moves.append(''.join(temp))
	return possibleM(move, start+1)



# print(possibleMoves("++++"))

'''
input: string
output: boolean

"--++" --> False
"----" --> True
'''

def possibleWin(move):
	return possibleWinning(move, 0)

def possibleWinning(move, count):
	pMoves = possibleMoves(move)
	if len(pMoves) == 0:
		if count % 2 == 0:
			return True
		else:
			return False
	for move in pMoves:
		return possibleWinning(move, count+1)


# print("Did you win: {0}".format(possibleWin("--++")))
print("Did you win: {0}".format(possibleWin("----+-+++-++----++-")))
