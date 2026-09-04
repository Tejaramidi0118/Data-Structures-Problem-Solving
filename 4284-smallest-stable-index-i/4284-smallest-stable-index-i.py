class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        mini = [0]*n

        mini[-1] = nums[-1]

        for i in range(n-2,-1,-1):
            mini[i] = min(mini[i+1],nums[i])
        
        maxi = nums[0]

        for i in range(n):
            maxi = max(maxi,nums[i])

            if maxi - mini[i] <= k:
                return i
        
        return -1