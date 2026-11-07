class Solution:
    def countValidSubstrings(self, s: str) -> int:
        count = 0

        idx = -1

        for i in range(len(s)):
            if i >= 2 and (s[i-2] == 'a' and s[i-1] == 'b' and s[i] == 'c'):
                idx = i - 2
            
            count += i - idx
        
        return count