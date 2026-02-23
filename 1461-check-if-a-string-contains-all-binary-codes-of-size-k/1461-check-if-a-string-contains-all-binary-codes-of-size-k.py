class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 2 ** k
        
        if len(s) < needed + k - 1:
            return False
        
        seen = set()
        
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            
            if len(seen) == needed:
                return True
        
        return len(seen) == needed