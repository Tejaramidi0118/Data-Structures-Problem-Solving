class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        lst = []
        
        for row in grid:
            for e in row:
                lst.append(e)

        # Check feasibility
        rem = lst[0] % x
        for ele in lst:
            if ele % x != rem:
                return -1

        lst.sort()
        target = lst[len(lst) // 2]

        op = 0
        for val in lst:
            op += abs(val - target) // x

        return op