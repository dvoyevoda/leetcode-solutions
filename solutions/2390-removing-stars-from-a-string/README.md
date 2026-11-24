<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoicmVtb3Zpbmctc3RhcnMtZnJvbS1hLXN0cmluZyIsInByb2JsZW0iOnsidGl0bGUiOiJSZW1vdmluZyBTdGFycyBGcm9tIGEgU3RyaW5nIiwiZnJvbnRlbmRJZCI6IjIzOTAiLCJkaWZmaWN1bHR5IjoiTWVkaXVtIiwidG9waWNzIjpbXX0sInJvd3MiOlt7ImlkIjoiMjIwMjg1NDE0NCIsImxhbmd1YWdlIjoicHl0aG9uMyIsImFjY2VwdGVkQXQiOiIyMDI2LTExLTI0VDIwOjU5OjI4LjAyOVoiLCJzdGF0cyI6eyJydW50aW1lIjoiOTEgbXMiLCJtZW1vcnkiOiIyMC40IE1CIiwicnVudGltZVBlcmNlbnRpbGUiOjU0LjQ0LCJtZW1vcnlQZXJjZW50aWxlIjo1NS42OSwidG90YWxUZXN0cyI6NjUsInRlc3RzUGFzc2VkIjo2NX19XX0= -->

# 2390. Removing Stars From a String

![Medium difficulty](https://img.shields.io/badge/Difficulty-Medium-A65E00?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/removing-stars-from-a-string/submissions/2202854144/) | 91 ms (beats 54.44%) | 20.4 MB (beats 55.69%) | 65/65 | 2026-11-24 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            elif stack:
                stack.pop()
        
        return "".join(stack)
```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
