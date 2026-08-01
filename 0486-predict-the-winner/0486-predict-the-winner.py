class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        d = {}

        def game(i,j):
            if i == j:
                return nums[i]
            
            if (i,j) in d:
                return d[(i,j)]
            
            left = nums[i] - game(i+1,j)
            right = nums[j] - game(i,j-1)

            d[(i,j)] = max(left, right)

            return d[(i,j)]
        
        return game(0,len(nums)-1) >= 0