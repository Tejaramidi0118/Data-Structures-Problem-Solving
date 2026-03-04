class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = mat[i][j]

        count = 0
        
        for i in range(rows):
            if mat[i].count(1) == 1:
                j = mat[i].index(1)
                
                if transposed[j].count(1) == 1:
                    count += 1
        
        return count