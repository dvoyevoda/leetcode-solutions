class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueChars = {}
        for i in range (len(s)):
            if s[i] in uniqueChars:
                uniqueChars[s[i]] += 1
            else:
                uniqueChars[s[i]] = 1
        for i in range (len(s)):
            if uniqueChars[s[i]] == 1:
                return i
        return -1