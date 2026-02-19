class Solution:
    def minInsertions(self, s: str) -> int:
        def longestCommonSubsequence(text1, text2):
            m = len(text1)
            n = len(text2)

            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if text1[j-1] == text2[i-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[n][m]

        lcs = longestCommonSubsequence(s,s[::-1])

        return len(s) - lcs