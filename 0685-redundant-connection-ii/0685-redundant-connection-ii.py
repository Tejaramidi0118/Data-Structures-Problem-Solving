class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        indegree = {i: None for i in range(1, n + 1)}

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

        conflict, cycle = None, None

        for u, v in edges:
            if indegree[v] is not None:
                conflict = [u, v]
            else:
                indegree[v] = u
                if not union(u, v):
                    cycle = [u, v]

        if conflict is None:
            return cycle
                       
        if cycle:
            return [indegree[conflict[1]], conflict[1]]
        else:
            return conflict
