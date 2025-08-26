class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d = 0
        a = 0 
        for i in range(len(dimensions)):
            l, w = dimensions[i][0], dimensions[i][1]

            dl = ((l * l) + (w * w))
            al = l * w

            if (dl > d) or (d == dl and l * w > a):
                d = dl
                a = l * w
        
        return a