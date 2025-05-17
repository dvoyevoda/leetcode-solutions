class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        wordsWithX = []
        for index, word in enumerate(words):
            for char in word:
                if char == x:
                    wordsWithX.append(index)
                    break
        return wordsWithX