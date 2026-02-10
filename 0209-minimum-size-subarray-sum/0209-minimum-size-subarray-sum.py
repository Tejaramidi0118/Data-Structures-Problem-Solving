class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        if max(nums) >= target:
            return 1
        
        k = float('inf')
        n = len(nums)

        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                k = min(k, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return k if k != float('inf') else 0