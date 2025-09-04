class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        n = 0

        for i in nums:
            if i % 6 == 0:
                s += i
                n += 1
        if s == 0:
            return 0
        else:
            return s//n