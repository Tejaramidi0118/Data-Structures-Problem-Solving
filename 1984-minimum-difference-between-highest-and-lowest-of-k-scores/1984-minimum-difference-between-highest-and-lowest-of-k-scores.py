class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        
        minDiff = float('inf')

        for i in range(len(nums) - k + 1):
            diff = nums[i + k -1] - nums[i]

            minDiff = min(minDiff, diff)
        
        return minDiff


