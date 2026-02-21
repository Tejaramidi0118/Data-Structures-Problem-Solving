class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        primeNums = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        
        for i in range(left,right+1):
            if bin(i).count("1") in primeNums:
                count += 1

        return count       