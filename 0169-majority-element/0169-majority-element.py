class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) // 2

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        maxi = float('-inf')

        for k, v in freq.items():
            if v > limit:
                if maxi < k:
                    maxi = k
        
        return maxi