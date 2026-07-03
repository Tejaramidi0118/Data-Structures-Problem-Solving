class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1

        maxJumps = nums[0]

        if maxJumps >= n:
            return True

        pos = 0

        while pos <= maxJumps:
            maxJumps = max(maxJumps,pos+nums[pos])

            if maxJumps >= n:
                return True
            
            pos += 1
        
        return False