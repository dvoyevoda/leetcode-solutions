class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = curr = 0
        seen = set()

        for curr in range(len(s)):
            while s[curr] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[curr])
            ans = max(ans, curr - left + 1)

        return ans

