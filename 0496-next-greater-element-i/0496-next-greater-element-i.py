class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_maxi = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            
            next_maxi[num] = -1 if not stack else stack[-1]
            stack.append(num)

        return [next_maxi[num] for num in nums1]