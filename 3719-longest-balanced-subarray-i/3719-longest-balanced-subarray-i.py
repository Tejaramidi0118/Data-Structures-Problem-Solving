class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        length = 0

        for i in range(n):
            odd_set = set()
            even_set = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])

                if len(odd_set) == len(even_set):
                    length = max(length, j - i + 1)

        return length