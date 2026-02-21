class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**(0.5))+1):
                if n % i == 0:
                    return False

            return True

        def countBits(n):
            ones = 0
            while n > 0:
                x = n % 2
                if x == 1:
                    ones += 1
                n //= 2

            return ones

        count = 0
        for i in range(left,right+1):
            if isPrime(countBits(i)):
                count += 1
            
        return count