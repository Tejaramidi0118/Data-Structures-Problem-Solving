class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            else:
                result.append(nums[(i + nums[i]) % len(nums)])
        
        return result