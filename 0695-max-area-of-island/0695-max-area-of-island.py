class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isSafe(r, c):
            return (0 <= r < len(grid)) and \
                   (0 <= c < len(grid[0])) and \
                   (grid[r][c] == 1) and \
                   (not visited[r][c])

        def dfs(r, c):
            visited[r][c] = True
            area = 1
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isSafe(nr, nc):
                    area += dfs(nr, nc)
            return area

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if isSafe(r, c):
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)

        return max_area
