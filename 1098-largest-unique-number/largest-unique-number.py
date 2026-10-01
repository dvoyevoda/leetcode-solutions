class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        freq_map = defaultdict(int)
        largest = -1
        
        for num in nums:
            freq_map[num] += 1
            
        for num in freq_map:
            if freq_map[num] == 1:
                largest = max(num, largest)
            
        return largest