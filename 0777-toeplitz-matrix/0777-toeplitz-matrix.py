class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        freq = dict()

        for i in range(m):
            for j in range(n):
                diff = i - j
                if diff in freq:
                    freq[diff].append(matrix[i][j])
                else:
                    freq[diff] = [matrix[i][j]]

        
        for v in freq.values():
            value = v[0]
            for val in v:
                if val != value:
                    return False
        return True
            
                