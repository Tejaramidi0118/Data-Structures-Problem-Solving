class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        sufSum = [0] * (n+1)

        for i in range(n-1,-1,-1):
            sufSum[i] = sufSum[i+1] + piles[i]
        
        d = {}

        def game(i,M):
            if i >= n:
                return 0
            
            if i + 2*M >= n:
                return sufSum[i]
            
            if (i,M) in d:
                return d[(i,M)]
            
            best = 0

            for X in range(1,2*M+1):
                oppScore = game(i+X,max(M,X))

                curr = sufSum[i] - oppScore

                best = max(best,curr)
            
            d[(i,M)] = best

            return best
        
        return game(0,1)