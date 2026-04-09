class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_array = [nums[0]]
        for i in range(1, len(nums)):
            prefix_array.append(nums[i] + prefix_array[-1])
        
        return max(1,1 - min(prefix_array))
        