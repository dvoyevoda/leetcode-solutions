class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start]
        XOR_total = start
        for i in range(1,n):
            nums.append(start + 2 * i)
            XOR_total ^= nums[i]
        return XOR_total
