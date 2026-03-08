class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""

        for i in range(len(nums)):
            if nums[i][i] == '1':
                res += '0'
            else:
                res += '1'
        
        return res