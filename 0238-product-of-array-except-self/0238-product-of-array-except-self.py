class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        product = nums[0]
        for i in range(1, len(nums)):
            res[i] = product
            product *= nums[i]
        
        print(res)
        product = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * product
            product *= nums[i]
        
        return res