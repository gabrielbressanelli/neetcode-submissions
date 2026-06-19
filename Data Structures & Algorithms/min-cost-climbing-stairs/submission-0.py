class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        x, y = cost[0], cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(x, y)

            x = y
            y = current

        return min(x, y)
            
