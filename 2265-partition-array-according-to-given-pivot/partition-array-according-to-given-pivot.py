class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        below_pivot = []
        above_pivot = []
        equal_pivot = []
        for num in nums:
            if num < pivot:
                below_pivot.append(num)
            if num == pivot:
                equal_pivot.append(num)
            if num > pivot:
                above_pivot.append(num)
        return below_pivot + equal_pivot + above_pivot
