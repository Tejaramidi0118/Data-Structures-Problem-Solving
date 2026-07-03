class Solution:
    def jump(self, nums: List[int]) -> int:
        curr, jump = 0,0
        count = 0

        for i in range(len(nums)-1):
            jump = max(jump,i+nums[i])

            if i == curr:
                curr = jump
                count += 1
        
        return count
