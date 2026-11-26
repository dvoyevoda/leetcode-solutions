class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = defaultdict(int)
        ans = []

        for num in nums:
            freq_map[num] += 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq_map:
            freq_buckets[freq_map[num]].append(num)
        
        count = k

        for nums in reversed(freq_buckets):
            for num in nums:
                if count > 0:
                    ans.append(num)
                    count-=1
                else:
                    break


        return ans

