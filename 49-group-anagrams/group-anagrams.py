class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            if key in groupMap:
                groupMap[key].append(word)
            else:
                groupMap[key] = [word]

        return list(groupMap.values())