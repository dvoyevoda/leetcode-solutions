class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        str_num = str(num)
        for i in range (len(str_num)):
            if num % int(str_num[i]) == 0:
                count += 1
        return count