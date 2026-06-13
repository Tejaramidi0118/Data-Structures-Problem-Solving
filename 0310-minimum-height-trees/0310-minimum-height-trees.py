class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            degree[u] += 1
            graph[v].append(u)
            degree[v] += 1

        leaves = deque()

        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)