class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_map = defaultdict(int)
        
        for char in text:
            freq_map[char] += 1
            
        freq_map['l'] //= 2
        freq_map['o'] //= 2
        
        return min(freq_map['b'],freq_map['a'],freq_map['l'],freq_map['o'],freq_map['n'])
        