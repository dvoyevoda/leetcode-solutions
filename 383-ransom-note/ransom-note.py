class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map_magazine = defaultdict(int)

        for char in magazine:
            freq_map_magazine[char] += 1
        
        for char in ransomNote:
            if char in freq_map_magazine:
                if freq_map_magazine[char] == 0:
                    return False
                else:
                    freq_map_magazine[char] -= 1
            else:
                return False
        
        return True