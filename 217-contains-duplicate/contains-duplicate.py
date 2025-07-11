class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for n in nums:
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        
        for value in freq_map.values():
            if value >= 2:
                return True
            
        return False