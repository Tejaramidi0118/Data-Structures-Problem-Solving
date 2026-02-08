class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 1
        left = 0

        for right in range(n):
            while left <= right:
                mid = (left + right) // 2

                left_cost = nums[mid] * (mid - left) - (prefix[mid] - prefix[left])

                right_cost = (prefix[right + 1] - prefix[mid + 1]) - nums[mid] * (right - mid)

                total_cost = left_cost + right_cost

                if total_cost <= k:
                    break
                left += 1

            ans = max(ans, right - left + 1)

        return ans
