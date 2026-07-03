class Solution:
    def largestNumber(self, nums: List[int]) -> str:


        for i in range(1,len(nums)):
            key = str(nums[i])
            j = i-1
            while j >= 0 and int(str(nums[j])+key) < int(key+str(nums[j])):
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = int(key)
        

        if nums[0] == 0:
            return "0"
        
        return "".join(map(str,nums))