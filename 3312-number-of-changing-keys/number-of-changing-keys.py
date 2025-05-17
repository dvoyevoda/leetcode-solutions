class Solution:
    def countKeyChanges(self, s: str) -> int:
        current_key = s[0]
        count = 0
        for char in s:
            if char != current_key and char.lower() != current_key:
                if char != current_key.lower() and char.lower() != current_key:
                    count += 1
            current_key = char
        return count
