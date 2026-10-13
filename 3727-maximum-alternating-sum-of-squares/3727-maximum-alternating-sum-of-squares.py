class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        

        nums = [num ** 2 for num in nums]
        nums.sort()

        res = 0
        for i in range(len(nums)):
            if i < (len(nums)) // 2:
                res -= nums[i]
            else:
                res += nums[i]
        return res
        