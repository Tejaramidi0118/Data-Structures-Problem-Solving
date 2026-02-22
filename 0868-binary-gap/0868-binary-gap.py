class Solution:
    def binaryGap(self, n: int) -> int:
        
        binNum = bin(n)[2:]
        prev = -1
        maxi = 0
        
        for i in range(len(binNum)):
            if binNum[i] == '1':
                if prev != -1:
                    maxi = max(maxi, i - prev)
                prev = i
        
        return maxi