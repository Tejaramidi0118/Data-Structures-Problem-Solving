class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def bs(n1, key):
            l, r = 0, len(n1) - 1
            while l <= r:
                m = (l + r) // 2
                if n1[m] == key:  
                    n1.insert(m,key)
                    return
                elif key > n1[m]:
                    l = m + 1
                else:
                    r = m - 1
            n1.insert(l, key)
        
        for i in nums2:
            bs(nums1,i)

        n = len(nums1)
        if len(nums1) % 2 == 1:
            return nums1[len(nums1)//2]
        else:
            return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        