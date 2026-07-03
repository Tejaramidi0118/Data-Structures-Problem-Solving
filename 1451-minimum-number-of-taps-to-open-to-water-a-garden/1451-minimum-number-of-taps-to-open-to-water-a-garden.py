class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []

        for i, r in enumerate(ranges):
            intervals.append([max(0, i-r), min(n, i+r)])
        
        intervals.sort(key = lambda x:x[0])
        
        s = 0
        i = 0
        ans = 0

        while s < n:
            far = s

            while i < len(intervals) and intervals[i][0] <= s:
                far = max(far, intervals[i][1])
                i += 1
            
            if far == s:
                return -1
            
            s = far
            ans += 1
        
        return ans