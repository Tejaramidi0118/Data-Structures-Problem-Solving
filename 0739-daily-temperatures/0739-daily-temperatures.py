class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i,temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i-j

            stack.append(i)
    
        return res