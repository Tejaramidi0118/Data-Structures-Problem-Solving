class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preSum = [0 for _ in range(len(nums ))]

        preSum[0] = nums[0]

        for i in range(1,len(nums)):
            preSum[i] = preSum[i-1] + nums[i]
        
        return preSum