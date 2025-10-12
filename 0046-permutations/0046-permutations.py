class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], result)
        return result

    def backtrack(self, nums, path, result):
        if len(path) == len(nums):
            result.append(list(path))
        else:
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                self.backtrack(nums, path, result)
                path.pop()
