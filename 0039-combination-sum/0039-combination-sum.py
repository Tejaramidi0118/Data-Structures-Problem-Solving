class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, 0, target, [], result)
        return result

    def backtrack(self, candidates, start, target, path, result):
        if target == 0:
            result.append(list(path))
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates, i, target - candidates[i], path, result)
            path.pop()
