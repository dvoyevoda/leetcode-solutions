class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_set = set(arr)
        total = 0

        for num in arr:
            if (num + 1) in num_set:
                total += 1

        return total