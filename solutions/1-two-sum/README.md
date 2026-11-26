<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoidHdvLXN1bSIsInByb2JsZW0iOnsidGl0bGUiOiJUd28gU3VtIiwiZnJvbnRlbmRJZCI6IjEiLCJkaWZmaWN1bHR5IjoiRWFzeSIsInRvcGljcyI6W119LCJyb3dzIjpbeyJpZCI6IjIyMDQxODE2MjQiLCJsYW5ndWFnZSI6InB5dGhvbjMiLCJhY2NlcHRlZEF0IjoiMjAyNi0xMS0yNlQyMDo1MjoyOS4yMDJaIiwic3RhdHMiOnsicnVudGltZSI6IjEgbXMiLCJtZW1vcnkiOiIyMSBNQiIsInJ1bnRpbWVQZXJjZW50aWxlIjo2Ni4wNywibWVtb3J5UGVyY2VudGlsZSI6NS45MiwidG90YWxUZXN0cyI6NjYsInRlc3RzUGFzc2VkIjo2Nn19XX0= -->

# 1. Two Sum

![Easy difficulty](https://img.shields.io/badge/Difficulty-Easy-137B59?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/two-sum/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/two-sum/submissions/2204181624/) | 1 ms (beats 66.07%) | 21 MB (beats 5.92%) | 66/66 | 2026-11-26 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in pairs:
                return [i, pairs[compliment][1]]
            pairs[num] = (target - num, i)
        
       
        #   2 = 7, 0
        #   7 = 2, 1
        #   11 = -2, 2
        #   15 = -6, 3
```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
