from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]  # (time, node)
        visited = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = time

            for neigh, weight in graph[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (time + weight, neigh))

        return max_time if len(visited) == n else -1