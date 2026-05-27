class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = right // 2

        while left <= right:
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

            middle = left + (right - left) // 2



        return -1
        