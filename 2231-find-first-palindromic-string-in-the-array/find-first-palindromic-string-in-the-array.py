class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            word_length = len(word)
            is_Palindrome = True
            for i in range (word_length // 2):
                if word[i] != word[word_length-i-1]:
                    is_Palindrome = False
                    break
            if is_Palindrome:
                return word
        return ""