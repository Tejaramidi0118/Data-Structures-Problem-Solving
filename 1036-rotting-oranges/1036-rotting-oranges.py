from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        for row in grid:
            for v in row:
                if v == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        maxT = 0

        while q:
            r,c,t = q.popleft()
            maxT = t

            for dr,dc in dirs:
                if 0 <= r + dr < len(grid) and 0 <= c+dc < len(grid[0]):
                    newR, newC = r+dr, c+dc

                    if grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        fresh -= 1
                    
                        q.append((newR,newC,t+1))
            
        
        return maxT if fresh == 0 else -1