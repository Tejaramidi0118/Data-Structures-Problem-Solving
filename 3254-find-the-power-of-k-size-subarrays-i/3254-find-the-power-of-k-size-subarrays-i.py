class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)
        left = 0
        for right in range(len(nums)):
            if right > 0 and nums[right] != nums[right - 1] + 1:
                left = right
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                res[left] = nums[right]
        
        return res