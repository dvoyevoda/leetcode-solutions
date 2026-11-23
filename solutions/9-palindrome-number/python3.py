class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0] == '-':
            return False
        num = ''
        for i in str(x):
            num = i + num
        if int(num) == x:
            return True
        else:
            return False