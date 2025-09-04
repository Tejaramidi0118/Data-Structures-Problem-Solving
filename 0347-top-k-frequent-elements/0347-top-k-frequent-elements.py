import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for i in nums:
            d[i] = d.setdefault(i, 0) + 1

        heap = []

        for key, val in d.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [key for (val, key) in heap]