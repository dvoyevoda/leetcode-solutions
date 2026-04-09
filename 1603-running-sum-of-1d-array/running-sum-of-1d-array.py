class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_array = [nums[0]]
        for i in range(1, len(nums)):
            prefix_array.append(nums[i] + prefix_array[-1])
        
        return prefix_array