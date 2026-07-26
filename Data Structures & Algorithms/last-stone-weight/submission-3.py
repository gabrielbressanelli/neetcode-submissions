class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        while len(stones) > 1:
            stones.sort()
            if stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()

            elif stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
                
        if stones: 
            return stones[0] 
        else: 
            return 0

        