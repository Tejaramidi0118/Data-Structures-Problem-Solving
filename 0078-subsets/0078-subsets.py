class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result
    
    def backtrack(self, nums: List[int], start: int, path: List[int], result: List[List[int]]):
        result.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, result)
            path.pop()
