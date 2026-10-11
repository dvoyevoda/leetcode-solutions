class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = deque()
        ans = []

        for i, val in enumerate(nums):

            while window and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] <= val:
                window.pop()

            window.append(i)

            if i >= k - 1:
                ans.append(nums[window[0]])
            
        return ans