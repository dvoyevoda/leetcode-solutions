class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        while (num > 9):
            numStr = str(num)
            num = 0
            for i in range(len(numStr)):
                num += int(numStr[i])
        return num
