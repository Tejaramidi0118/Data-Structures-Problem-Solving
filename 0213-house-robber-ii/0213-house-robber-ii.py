class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                temp = max(prev1,prev2+num)
                prev2 = prev1
                prev1 = temp
            
            return prev1

        return max(rob(nums[1:]),rob(nums[:-1]))