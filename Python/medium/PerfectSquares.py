def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        dp=[1]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            if i in squares:
                continue
            dp[i]=dp[i-1]+1
            for square in squares:
                if i < square:
                    break
                dp[i]=min(dp[i], dp[i-square]+1)
        return dp[-1]