class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through the list, check if the element before is equal the element, if so, remove that element
        # we can start at index 1
        # if the list is less than 2, return 1.

        if len(nums) < 2:
            return 1
        else:
            i = 1
            while i < len(nums):
                if nums[i-1] == nums[i]:
                    nums.pop(i)
                else:
                    i += 1
            return len(nums)
            
