class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n,n+t+1):
            p = 1
            temp = i

            while temp != 0:
                p *= temp%10
                temp //= 10

            if p % t == 0:
                return i
                    