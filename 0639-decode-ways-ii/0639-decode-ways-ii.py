class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        def single(c):
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1

        def pair(a, b):
            if a == '*' and b == '*':
                return 15
            if a == '*':
                if '0' <= b <= '6':
                    return 2
                else:
                    return 1
            if b == '*':
                if a == '1':
                    return 9
                if a == '2':
                    return 6
                return 0
            return 1 if 10 <= int(a+b) <= 26 else 0

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = single(s[0])

        for i in range(2, n+1):
            dp[i] += single(s[i-1]) * dp[i-1]
            dp[i] += pair(s[i-2], s[i-1]) * dp[i-2]
            dp[i] %= MOD

        return dp[n]