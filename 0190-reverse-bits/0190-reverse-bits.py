class Solution:
    def reverseBits(self, n: int) -> int:
        s = ""
        
        for _ in range(32):
            s += str(n % 2)
            n //= 2
        
        return int(s, 2)
