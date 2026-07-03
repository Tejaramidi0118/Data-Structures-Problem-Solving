class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff = []
        for cost in costs:
            diff.append(cost+[cost[0]-cost[1]])
        
        diff.sort(key=lambda d: d[2])
        fly = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                fly += diff[i][0]
            else:
                fly += diff[i][1]
        
        return fly