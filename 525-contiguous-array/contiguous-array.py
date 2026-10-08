class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_sum = 0
        prefix_map = {0: -1}
        max_length = 0

        for i in range(0, len(nums)):

            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1

            if running_sum not in prefix_map:
                prefix_map[running_sum] = i
            else:
                max_length = max(max_length, (i - prefix_map[running_sum]))

        return max_length
        
    