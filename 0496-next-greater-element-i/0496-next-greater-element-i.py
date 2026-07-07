class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [-1 for _ in range(len(nums2))]
        stack = []

        for i,num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                j = stack.pop()
                nge[j] = num
            
            stack.append(i)
        
        res = []

        for num in nums1:
            idx = nums2.index(num)
            res.append(nge[idx])
        
        return res