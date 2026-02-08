class Solution:
    def minimumDeletions(self, s: str) -> int:
        minDel = 0
        count_b = 0

        for ch in s:
            if ch == 'b':
                count_b += 1
            elif count_b:
                minDel += 1
                count_b -= 1
        
        return minDel