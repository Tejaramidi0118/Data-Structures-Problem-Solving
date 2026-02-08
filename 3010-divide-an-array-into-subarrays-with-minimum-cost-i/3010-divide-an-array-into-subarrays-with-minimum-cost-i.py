class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]

        nums = nums[1:]
        
        cost += min(nums)

        nums.remove(min(nums))

        cost += min(nums)

        return cost