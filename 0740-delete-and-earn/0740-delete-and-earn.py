class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        dp = [0] * (max(nums) + 1)

        dp[1] = count[1] * 1

        for i in range(2, max(nums)+1):
            take = dp[i-2] + count[i]*i
            skip = dp[i-1]

            dp[i] = max(take,skip)
        
        return dp[-1]