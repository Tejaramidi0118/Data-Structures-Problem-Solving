from collections import deque	
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        
        fresh_oranges = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        max_time = 0
        
        while q:
            r,c,time = q.popleft()
            max_time = time
            
            for dr,dc in directions:
                new_r, new_c = r+dr, c+dc
                
                if 0 <= new_r < rows and 0 <= new_c < cols and \
                grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    
                    q.append((new_r,new_c,time+1))
                    
                    fresh_oranges -= 1

        if fresh_oranges == 0:
            return max_time
        else:
            return -1