class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)

        prefix = [0]*(n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        prod = 1
        ans = float('inf')

        for i in range(n-1, -1, -1):

            if i+1 < n:
                prod *= nums[i+1]

            if prod > prefix[i]:
                prod = prefix[i] + 1

            if prod == prefix[i]:
                ans = min(ans, i)

        return ans if ans != float('inf') else -1