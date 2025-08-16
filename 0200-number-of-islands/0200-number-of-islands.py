from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isSafe(grid,r,c,visited):
            return (0 <= r < len(grid)) and \
                   (0 <= c < len(grid[0])) and \
                   (grid[r][c] == '1') and \
                   (not visited[r][c])

        def dfs(grid,r,c,visited):
            directions = [(-1,0),(0,-1),(0,1),(1,0)]
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isSafe(grid,nr,nc,visited):
                    dfs(grid,nr,nc,visited)

        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        output = 0

        for r in range(rows):
            for c in range(cols):
                if isSafe(grid,r,c,visited):
                    dfs(grid,r,c,visited)
                    output += 1
        return output
