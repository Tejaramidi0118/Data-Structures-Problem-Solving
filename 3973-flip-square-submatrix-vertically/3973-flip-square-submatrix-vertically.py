class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        left = x
        right = left + k - 1

        while left <= right:
            l_row = grid[left]
            r_row = grid[right]

            for idx in range(y, y + k):
                l_row[idx], r_row[idx] = r_row[idx], l_row[idx]
            
            left += 1
            right -= 1
        return grid

