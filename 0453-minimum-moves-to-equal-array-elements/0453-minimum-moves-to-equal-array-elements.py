class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        return sum(nums) - (len(nums) * min(nums))