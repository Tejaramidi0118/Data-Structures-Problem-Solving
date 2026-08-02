class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        i = 0
        even, odd = 0, 0

        while i < len(piles):
            if i % 2 == 0:
                even += piles[i]
            else:
                odd += piles[i]
            
            i += 1
            
        return even > odd or even <= odd