class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        out = []
        maxi = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                out.append(True)
            else:
                out.append(False)
        
        return out