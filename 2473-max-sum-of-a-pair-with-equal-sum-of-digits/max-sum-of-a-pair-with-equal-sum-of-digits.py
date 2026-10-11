class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        max_num = {}
        ans = -1

        for num in nums:
            digit_sum = sum(map(int, str(num)))

            if digit_sum in max_num:
                ans = max(ans, num + max_num[digit_sum])
                max_num[digit_sum] = max(max_num[digit_sum], num)

            else:
                max_num[digit_sum] = num
        return ans
