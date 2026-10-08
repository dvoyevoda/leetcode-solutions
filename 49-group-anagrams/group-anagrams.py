class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_map = defaultdict(list)
        for str in strs:
            group_map["".join(sorted(str))].append(str)
        
        return list(group_map.values())

