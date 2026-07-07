class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        temp = 0
        for ch in s:
            if ch == '(':
                temp += 1
                maxi = max(maxi,temp)
            elif ch ==')':
                temp -= 1
        
        return maxi