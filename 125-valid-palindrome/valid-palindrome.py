class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        i = 0
        j = len(normalized) - 1
        for i in range(j):
            if normalized[i] != normalized[j]:
                return False
            j -= 1
        return True