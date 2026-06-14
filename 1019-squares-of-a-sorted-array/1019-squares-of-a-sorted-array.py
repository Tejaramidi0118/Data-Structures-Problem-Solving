class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        out = []

        for num in nums:
            out.append((num)**2)
        
        return sorted(out)