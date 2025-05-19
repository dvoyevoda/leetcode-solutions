class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_Count = 0
        for num in arr:
            if num % 2 != 0:
                odd_Count += 1
            else:
                odd_Count = 0
            if odd_Count == 3:
                return True
        return False