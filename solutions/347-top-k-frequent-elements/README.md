<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoidG9wLWstZnJlcXVlbnQtZWxlbWVudHMiLCJwcm9ibGVtIjp7InRpdGxlIjoiVG9wIEsgRnJlcXVlbnQgRWxlbWVudHMiLCJmcm9udGVuZElkIjoiMzQ3IiwiZGlmZmljdWx0eSI6Ik1lZGl1bSIsInRvcGljcyI6W119LCJyb3dzIjpbeyJpZCI6IjIyMDM2NDYyMjUiLCJsYW5ndWFnZSI6InB5dGhvbjMiLCJhY2NlcHRlZEF0IjoiMjAyNi0xMS0yNlQwNTowMzo0OC4xMzBaIiwic3RhdHMiOnsicnVudGltZSI6IjExIG1zIiwibWVtb3J5IjoiMjQuNiBNQiIsInJ1bnRpbWVQZXJjZW50aWxlIjoyNC41MSwibWVtb3J5UGVyY2VudGlsZSI6MjIuNzEsInRvdGFsVGVzdHMiOjI2LCJ0ZXN0c1Bhc3NlZCI6MjZ9fV19 -->

# 347. Top K Frequent Elements

![Medium difficulty](https://img.shields.io/badge/Difficulty-Medium-A65E00?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/top-k-frequent-elements/submissions/2203646225/) | 11 ms (beats 24.51%) | 24.6 MB (beats 22.71%) | 26/26 | 2026-11-26 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
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

```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
