class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            for char in str(num):
                digit_sum += int(char)
        return abs(element_sum - digit_sum)