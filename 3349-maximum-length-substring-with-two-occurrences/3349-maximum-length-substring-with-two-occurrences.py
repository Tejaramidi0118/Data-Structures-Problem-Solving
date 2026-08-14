class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        l = 0
        maxi = 0
        r = 0

        while  r < len(s):
            freq[s[r]] += 1
            
            while l < len(s) and freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            
            maxi = max(maxi,r-l+1)

            r += 1
        
        return maxi