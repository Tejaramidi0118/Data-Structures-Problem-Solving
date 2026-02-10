class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        seen = set()

        for i in range(n):
            seen.clear()
            bal = 0
            if count > n - i:
                break
            for j in range(i, n):
                num = nums[j]
                if num not in seen: 
                    if num % 2:
                        bal -= 1
                    else:
                        bal += 1
                    seen.add(num)
                if bal == 0:
                    count = max(count, j - i + 1)
        
        return count
                