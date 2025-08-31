from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = {i: [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = float("inf")

        def bfs(start):
            dist = [-1] * n
            parent = [-1] * n
            q = deque([start])
            dist[start] = 0
            shortest = float("inf")

            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        shortest = min(shortest, dist[u] + dist[v] + 1)
            return shortest

        for i in range(n):
            ans = min(ans, bfs(i))

        return -1 if ans == float("inf") else ans
