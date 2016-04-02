maxsize = 0
size = 0
countArray = []
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        global maxsize
        global size
        global countArray
        
        countArray = [[0]*len(A[0])]*len(A)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.findMaxRectangle(A, i, j, len(A), len(A[0]), 0)
        
        return maxsize
        
    def findMaxRectangle(self, A, x, y, maxRow, maxCol, size):
        global maxsize
        global countArray
        
        if x >= maxRow or y >= maxCol:
            return
        size += 1
        countArray[x][y] = 1
        
        if size > maxsize:
            maxsize = size
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        
        for i in range(0, 4):
            newi = x+directions[i][0]
            newj = y+directions[i][1]
            val = self.getVal(A, newi, newj)
            if val > 0 and countArray[newi][newj] == 0:
                self.findMaxRectangle(A, newi, newj, maxRow, maxCol, size)
        countArray[x][y] = 0 
    
    def getVal(self, A, x, y):
        if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]):
            return 0
        else:
            return A[x][y]
        