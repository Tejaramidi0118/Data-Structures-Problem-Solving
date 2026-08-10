class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]

        for x in range(1,n+1):
            sq = 1

            while sq*sq <= x:
                if not dp[x-sq*sq]:
                    dp[x] = True
                    break

                sq += 1
        
        return dp[n]