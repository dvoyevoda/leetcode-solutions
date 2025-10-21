class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        counter = 0
        for index, x in enumerate(nums):
            if x == target:
                return index
            if x > target:
                return index
            if index == len(nums) - 1:
                return len(nums)