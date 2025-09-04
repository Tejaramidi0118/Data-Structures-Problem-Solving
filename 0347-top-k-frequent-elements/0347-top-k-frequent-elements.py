import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            d[i] = d.setdefault(i, 0) + 1
        
        sorted_d = [item[0] for item in sorted(d.items(), key=lambda item: item[1], reverse=True)]


        return sorted_d[:k]