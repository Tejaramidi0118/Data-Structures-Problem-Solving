import heapq
class Solution:
    def minNumberOfSeconds(self, mountainH: int, workerTimes: List[int]) -> int:
        pq = []

        for i in range(len(workerTimes)):
            heapq.heappush(pq,(workerTimes[i],i,1))

        
        res = 0

        while mountainH > 0:
            t, i, x = heapq.heappop(pq)

            res = t

            mountainH -= 1

            if mountainH > 0:
                nx = x + 1
                nt = workerTimes[i] * (nx*(nx+1)//2)
                heapq.heappush(pq,(nt,i,nx))
        
        return res