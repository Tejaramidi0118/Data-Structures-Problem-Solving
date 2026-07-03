import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                heap.append([arr[i]/arr[j], arr[i],arr[j]])

        heap.sort(key = lambda x:x[0])

        return [heap[k-1][1],heap[k-1][2]]