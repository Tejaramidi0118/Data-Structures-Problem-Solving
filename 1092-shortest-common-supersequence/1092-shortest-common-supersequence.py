class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
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
            
            i, j = n, m
            s = []

            while i > 0 and j > 0:
                if text1[j-1] == text2[i-1]:
                    s.append(text1[j-1])
                    i -= 1
                    j -= 1
                elif dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
            
            s.reverse()
            return "".join(s)
        

        lcs = longestCommonSubsequence(str1, str2)
        
        i = j = 0
        result = []

        for c in lcs:
            while str1[i] != c:
                result.append(str1[i])
                i += 1
            while str2[j] != c:
                result.append(str2[j])
                j += 1
            
            result.append(c)
            i += 1
            j += 1

        result.append(str1[i:])
        result.append(str2[j:])

        return "".join(result)