class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = 0
        place = 1
        s = 0
        while n > 0:
            d = n%10
            if d != 0:
                s += d
                num += d*place
                place *= 10

            n //= 10

        return num*s