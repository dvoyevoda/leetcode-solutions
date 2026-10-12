class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        splits = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        for i in range(len(prefix)-1):
            if prefix[i] >= (prefix[-1]) - prefix[i]:
                splits += 1
        return splits


        # 10, 14, 6, 13
