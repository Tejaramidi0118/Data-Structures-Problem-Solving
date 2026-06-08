class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(i,j):
            nonlocal count
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
        
        n = len(s)

        count = 0

        for i in range(n):
            palindrome(i,i)
            palindrome(i,i+1)
        
        return count