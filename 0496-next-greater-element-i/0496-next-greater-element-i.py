class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        res = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                res[nums2[idx]] = nums2[i]

            stack.append(i)

        return [res.get(i, -1) for i in nums1]