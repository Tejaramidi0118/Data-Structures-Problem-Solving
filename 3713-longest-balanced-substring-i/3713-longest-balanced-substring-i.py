class Solution:
    def longestBalanced(self, s: str) -> int:
        def isbalanced(d):
            return len(set(d.values())) == 1
        
        count_d = {}

        out = float('-inf')

        for i in range(len(s)):
            count_d = {}

            for j in range(i,len(s)):
                ch = s[j]

                count_d[ch] = count_d.get(ch,0) + 1

                if isbalanced(count_d):
                    out = max(out, j - i + 1)
        
        return out