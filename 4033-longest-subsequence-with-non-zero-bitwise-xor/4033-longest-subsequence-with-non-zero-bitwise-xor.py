class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0

        for num in nums:
            xor ^= num
        
        if xor != 0:
            return n
        
        return n-1 if any(nums) != 0 else 0