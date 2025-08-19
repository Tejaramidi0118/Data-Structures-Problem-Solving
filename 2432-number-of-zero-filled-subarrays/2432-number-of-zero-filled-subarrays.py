class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        output = 0
        n= len(nums)

        i = 0

        while i < n:
            if nums[i] == 0:

                j = i
                while j < n and nums[j] == 0:
                    j += 1
            
                run_length = j - i

                output += run_length * (run_length+1)//2

                i = j
            else:
                i += 1
        
        return output
        



        
