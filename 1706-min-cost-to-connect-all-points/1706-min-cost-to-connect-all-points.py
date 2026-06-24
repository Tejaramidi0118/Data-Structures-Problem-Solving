class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        included = [False for _ in range(n)]
        minDist = [float('inf') for _ in range(n)]

        minDist[0] = 0
        res = 0
        for i in range(n):
            u = -1
            best = float('inf')

            for i in range(n):
                if not included[i] and minDist[i] < best:
                    best = minDist[i]
                    u = i
            
            included[u] = True
            res += best

            x1,y1 = points[u]
            for v in range(n):
                if not included[v]:
                    x2,y2 = points[v]
                    dist = abs(x1-x2) + abs(y1-y2)
                    if dist < minDist[v]:
                        minDist[v] = dist
        
        return res