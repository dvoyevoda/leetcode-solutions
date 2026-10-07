class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = []
        double_digit = []

        for num in nums:
            if num < 10:
                single_digit.append(num)
            else:
                double_digit.append(num)
        
        return sum(single_digit) != sum(double_digit)