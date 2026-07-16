class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            
            return gcd(b,a%b)

        n = len(nums)
        prefixGcd = [0]*n
        maxi = nums[0]
        prefixGcd[0] = nums[0]

        for i in range(1,n):
            maxi = max(maxi,nums[i])
            prefixGcd[i] = gcd(nums[i],maxi)
        
        prefixGcd.sort()

        i,j = 0,n-1

        sumi = 0

        while i < j:
            sumi += gcd(prefixGcd[i],prefixGcd[j])

            i += 1
            j -= 1
        
        return sumi