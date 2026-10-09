class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])

        min_prefix = 0
        max_sum = nums[0]

        for i in range(0, len(prefix)):
            max_sum = max(max_sum, prefix[i] - min_prefix)
            min_prefix = min(prefix[i], min_prefix)

        return max_sum
        