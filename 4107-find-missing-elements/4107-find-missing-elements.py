class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        
        nums = set(nums)
        out = []

        for i in range(mini,maxi):
            if i not in nums:
                out.append(i)
        
        return out