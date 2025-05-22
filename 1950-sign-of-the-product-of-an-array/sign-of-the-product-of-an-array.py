class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        for num in nums:
            total *= num
        return 1 if total > 0 else 0 if total == 0 else -1
