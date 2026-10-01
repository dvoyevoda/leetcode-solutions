class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_map = defaultdict(int)
        balloon_count = 0
        
        for char in text:
            freq_map[char] += 1
            
        while True:
            if freq_map['b'] >= 1:
                freq_map['b'] -= 1
            else: break
            if freq_map['a'] >= 1:
                freq_map['a'] -= 1
            else: break
            if freq_map['l'] >= 2:
                freq_map['l'] -= 2
            else: break
            if freq_map['o'] >= 2:
                freq_map['o'] -= 2
            else: break
            if freq_map['n'] >= 1:
                freq_map['n'] -= 1
            else: break
            balloon_count += 1
        
        return balloon_count
        