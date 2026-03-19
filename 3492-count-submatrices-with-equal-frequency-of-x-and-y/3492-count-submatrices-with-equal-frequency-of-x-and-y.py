class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        sumX = [0]*n
        sumY = [0]*n

        for i in range(m):
            cx = 0
            cy = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    cx += 1
                elif grid[i][j] == 'Y':
                    cy += 1
                
                sumX[j] += cx
                sumY[j] += cy

                if sumX[j] > 0 and sumX[j] == sumY[j]:
                    count += 1
        
        return count