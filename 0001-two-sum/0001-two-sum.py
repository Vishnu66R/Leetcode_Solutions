class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i