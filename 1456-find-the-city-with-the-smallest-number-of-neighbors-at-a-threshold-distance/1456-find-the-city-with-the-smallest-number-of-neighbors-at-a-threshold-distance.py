from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0

            heap = [(0, src)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue

                for nei, w in graph[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(heap, (nd, nei))

            return dist

        best_city = -1
        best_count = float('inf')

        for city in range(n):
            dist = dijkstra(city)

            count = 0
            for i in range(n):
                if i != city and dist[i] <= distanceThreshold:
                    count += 1

            if count <= best_count:
                best_count = count
                best_city = city

        return best_city