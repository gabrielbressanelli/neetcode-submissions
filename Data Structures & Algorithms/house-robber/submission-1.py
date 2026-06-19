class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        x, y = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(nums[i]+x, y)
            x = y
            y = current

        return max(x, y)