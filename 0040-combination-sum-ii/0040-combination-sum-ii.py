class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(candidates, 0, target, [], result)
        return result

    def backtrack(self, candidates, start, target, path, result):
        if target < 0:
            return

        if target == 0:
            result.append(list(path))
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            path.append(candidates[i])
            self.backtrack(candidates, i + 1, target - candidates[i], path, result)
            path.pop()
