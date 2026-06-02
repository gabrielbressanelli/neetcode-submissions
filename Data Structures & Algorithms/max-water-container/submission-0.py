class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, (len(heights) - 1)
        most_water = 0

        while l < r:
            if heights[r] > heights[l]:
                total_water = heights[l] * (r-l)
                l +=1
                if total_water > most_water:
                    most_water = total_water
            else:
                total_water = heights[r] * (r-l)
                r -= 1
                if total_water > most_water:
                    most_water = total_water
        return most_water
                