class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in sentences:
            words = i.split(' ')
            if len(words) > max:
                max = len(words)
        return max