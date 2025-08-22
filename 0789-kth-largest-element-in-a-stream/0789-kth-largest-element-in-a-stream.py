import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kl = nums  # Store the list
        heapq.heapify(self.kl)  # Convert to Min Heap

        # Keep only the k largest elements
        while len(self.kl) > k:
            heapq.heappop(self.kl)

    def add(self, val: int) -> int:
        heapq.heappush(self.kl, val)  # Insert new value

        # If the heap size exceeds k, remove the smallest element
        if len(self.kl) > self.k:
            heapq.heappop(self.kl)

        return self.kl[0]  # The Kth largest element
