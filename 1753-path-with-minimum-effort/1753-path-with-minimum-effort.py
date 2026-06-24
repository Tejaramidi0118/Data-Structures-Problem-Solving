class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        hp = [(0, 0, 0)]
        vis = [[float('inf')] * n for _ in range(m)]
        vis[0][0] = 0
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        while hp:
            val, i, j = heapq.heappop(hp)
            
            if val > vis[i][j]:
                continue
            
            if i == m-1 and j == n-1:
                return val
            
            for xi, xj in dir:
                ti = i + xi
                tj = j + xj
                if 0 <= ti < m and 0 <= tj < n:
                    nval = max(val,abs(heights[i][j]- heights[ti][tj]))
                    if nval < vis[ti][tj]:
                        vis[ti][tj] = nval
                        heapq.heappush(hp,(nval, ti, tj))

        return vis[m-1][n-1]