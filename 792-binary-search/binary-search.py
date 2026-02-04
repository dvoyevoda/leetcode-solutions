class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = high // 2

        while low <= high:
            if target > nums[middle]:
                low = middle + 1
                middle = (high - low) // 2 + low
            elif target < nums[middle]:
                high = middle - 1
                middle = (high - low) // 2 + low
            if nums[middle] == target:
                return middle
        return -1