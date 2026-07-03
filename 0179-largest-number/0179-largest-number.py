from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        nums.sort(
            key=cmp_to_key(
                lambda a, b: -1 if a + b > b + a
                else 1 if a + b < b + a
                else 0
            )
        )

        if nums[0] == "0":
            return "0"

        return "".join(nums)