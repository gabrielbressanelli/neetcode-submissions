class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        min_rate = r

        while l <= r:
            mid = l + (r-l) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1)// mid

            if hours <= h:
                min_rate = mid
                r = mid - 1
                
            if hours > h:
                l = mid + 1

        return min_rate

            