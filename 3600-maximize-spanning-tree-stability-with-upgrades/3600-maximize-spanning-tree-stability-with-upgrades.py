class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        max_s = max(e[2] for e in edges)

        def check(X):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            opt_no_up = []
            opt_up = []

            for u,v,s,must in edges:
                if must == 1:
                    if s < X:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used += 1
            
            for u,v,s,must in edges:
                if must == 0:
                    if s >= X:
                        opt_no_up.append((u,v))
                    elif 2*s >= X:
                        opt_up.append((u,v))
            
            for u,v in opt_no_up:
                if dsu.union(u,v):
                    used += 1

                    if used == n-1:
                        return True
                

            for u,v in opt_up:
                if dsu.union(u,v):
                    upgrades += 1
                    used += 1
                    if upgrades > k:
                        return False
                    if used == n-1:
                        return True

            return used == n-1
            
        low, high = 1, 2*max_s
        ans = -1

        while low <= high:
            mid = (low+high) // 2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans