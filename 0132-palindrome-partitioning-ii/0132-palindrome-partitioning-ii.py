class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        isPal = [[False] * n for _ in range(n)]
        
        for end in range(n):
            for start in range(end + 1):
                if s[start] != s[end]:
                    continue
                
                length = end - start + 1
                
                if length <= 3:
                    isPal[start][end] = True
                else:
                    isPal[start][end] = isPal[start + 1][end - 1]
        
        dp = [0] * n
        
        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                
                for j in range(i):
                    if isPal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]