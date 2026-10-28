class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s)-1

        while left < right:
            left_char = s[left]
            right_char = s[right]
            s[left] = right_char
            s[right] = left_char
            right -= 1
            left += 1
        return s
        