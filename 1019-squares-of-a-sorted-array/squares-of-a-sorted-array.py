class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = 0
        right = length - 1
        result = [0] * length

        for i in range(length - 1, -1, -1):
            if (abs(nums[left]) < abs(nums[right])):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        
        return result


        return