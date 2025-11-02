class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        
        for i in nums:
            xor_sum |= i
        xor_sum *= (1 << n-1)
        
        return xor_sum