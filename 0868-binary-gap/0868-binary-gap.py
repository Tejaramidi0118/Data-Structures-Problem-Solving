class Solution:
    def binaryGap(self, n: int) -> int:
        maxi = 0

        binNum = bin(n)[2:]
        l = len(binNum)
        
        i = 0

        while i < l:
            while i < l and binNum[i] != '1':
                i += 1
            
            j = i + 1

            while j < l and binNum[j] != '1':
                j += 1
            
            if i < l and j < l:
                maxi = max(maxi, j - i)
                i = j
            else:
                break
        
        return maxi