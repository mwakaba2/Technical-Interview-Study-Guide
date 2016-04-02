def maxcoin(A):
        n = len(A)
        if n % 2:
            return -1
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = A[i]
        
        for no_coins in range(1, n):
            i = 0
            j = no_coins
            while j < n:
                if i == j - 1:
                    dp[i][j] = max(A[i], A[j])
                else:
                    a = dp[i+2][j] if i+2 <= j else 0
                    b = dp[i+1][j-1] if i+1 <= j - 1 else 0
                    c = dp[i][j-2] if i <= j - 2 else 0
                    dp[i][j] = max(A[i]+min(a, b), A[j]+min(b,c))
                i += 1
                j += 1
        print(dp)
        return dp[0][n-1]

maxcoin([200, 100, 500, 10])
