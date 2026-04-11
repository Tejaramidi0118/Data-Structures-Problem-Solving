class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}

        for i, num in enumerate(nums):
            d.setdefault(num, []).append(i)

        mini = float('inf')

        for v in d.values():
            if len(v) >= 3:
                for i in range(len(v) - 2):
                    dist = 2 * (v[i+2] - v[i])
                    mini = min(mini, dist)

        return mini if mini != float('inf') else -1