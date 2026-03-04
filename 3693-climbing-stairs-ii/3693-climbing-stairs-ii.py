class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for jump in range(1, 4):
                if i - jump >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i - jump] + costs[i] + jump * jump
                    )
        
        return dp[n]