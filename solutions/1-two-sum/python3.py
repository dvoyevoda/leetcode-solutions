class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in pairs:
                return [i, pairs[compliment][1]]
            pairs[num] = (target - num, i)
        
       
        #   2 = 7, 0
        #   7 = 2, 1
        #   11 = -2, 2
        #   15 = -6, 3
