class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)) :
            third_digit = target - nums[i]
            if third_digit in hash_map and i != hash_map[third_digit]:
                return [i, hash_map[third_digit]]

            