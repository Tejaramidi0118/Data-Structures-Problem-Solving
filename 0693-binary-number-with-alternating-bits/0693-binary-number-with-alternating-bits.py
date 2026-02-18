class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        r = ""

        while n > 0:
            r += str(n % 2)

            if len(r) > 1:
                if r[-2] == r[-1]:
                    return False

            n //= 2
        
        return True