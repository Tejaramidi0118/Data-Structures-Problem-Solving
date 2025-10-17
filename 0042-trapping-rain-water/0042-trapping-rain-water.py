class Solution:
    def trap(self, arr: List[int]) -> int:

        n = len(arr)
        
        l, r = 0, n -1
        
        lmax = rmax = trapped = 0
        
        
        while l < r:
            
            if arr[l] < arr[r]:
                
                lmax = max(lmax,arr[l])
                trapped += lmax - arr[l]
                
                l += 1
            
            else:
                rmax = max(rmax,arr[r])
                trapped += rmax - arr[r]
                
                r -= 1
        
        return trapped