class Solution:
    def countKeyChanges(self, s: str) -> int:
        current_key = s[0]
        count = 0
        for char in s:
            if char.lower() != current_key.lower():
                    count += 1
            current_key = char
        return count
