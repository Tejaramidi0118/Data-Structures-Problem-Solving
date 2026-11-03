class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)

        count = 0

        for num in nums:
            count += (maxi-num)

        return count