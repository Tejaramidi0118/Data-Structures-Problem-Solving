from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        dq = deque()

        for right in range(len(nums)):
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if right >= k - 1:
                output.append(nums[dq[0]])

        return output
