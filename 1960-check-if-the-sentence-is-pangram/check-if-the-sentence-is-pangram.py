class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        characters = set()
        for i in range(len(sentence)):
            characters.add(sentence[i])
        if len(characters) == 26:
            return True
        return False
        