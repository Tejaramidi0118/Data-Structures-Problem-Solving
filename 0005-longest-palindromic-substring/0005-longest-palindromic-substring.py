class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(i,j,n):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            
            return i+1,j-1
        
        lmax = rmax = 0
        n = len(s)

        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        
        for i in range(n):
            l1, r1 = palindrome(i, i, n)
            l2, r2 = palindrome(i, i+1, n)

            if r1-l1 > rmax - lmax:
                lmax, rmax = l1, r1
        
            if r2-l2 > rmax - lmax:
                lmax, rmax = l2, r2
            
            if rmax - lmax + 1 == len(s):
                return s 
        
        return s[lmax: rmax+1]        
