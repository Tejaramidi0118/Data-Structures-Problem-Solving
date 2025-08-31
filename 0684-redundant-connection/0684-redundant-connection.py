class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}

        def find_parent(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find_parent(x), find_parent(y)
            if px == py:
                return False
            parent[py] = px
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
