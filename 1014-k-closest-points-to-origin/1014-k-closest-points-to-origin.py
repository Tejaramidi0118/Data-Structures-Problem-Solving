import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        
        heapq.heapify(a)
        for x,y in points:
            dist = x**2 + y**2
            
            heapq.heappush(a,(-dist,[x,y]))
            
            if len(a) > k:
                heapq.heappop(a)
        
        
        return [point for (_,point) in a]
                    