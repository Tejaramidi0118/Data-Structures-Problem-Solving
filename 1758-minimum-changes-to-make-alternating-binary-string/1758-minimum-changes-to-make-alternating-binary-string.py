class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)

        s1 = "01"*(n//2 + 1)
        s2 = "10"*(n//2 + 1)

        res1, res2 = 0, 0

        for i in range(n):
            if s[i] != s1[i]:
                res1 += 1
            
            if s[i] != s2[i]:
                res2 += 1
        
        return min(res1,res2)