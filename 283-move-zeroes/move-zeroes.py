class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoneZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNoneZero] = nums[i]
                lastNoneZero += 1

        for i in range(lastNoneZero, len(nums)):
            nums[i] = 0
            
        