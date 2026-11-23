<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoicGFsaW5kcm9tZS1udW1iZXIiLCJwcm9ibGVtIjp7InRpdGxlIjoiUGFsaW5kcm9tZSBOdW1iZXIiLCJmcm9udGVuZElkIjoiOSIsImRpZmZpY3VsdHkiOiJFYXN5IiwidG9waWNzIjpbXX0sInJvd3MiOlt7ImlkIjoiMjIwMTU2OTE5MiIsImxhbmd1YWdlIjoicHl0aG9uMyIsImFjY2VwdGVkQXQiOiIyMDI2LTExLTIzVDAwOjI0OjQxLjkyN1oiLCJzdGF0cyI6eyJydW50aW1lIjoiMTggbXMiLCJtZW1vcnkiOiIxOS4yIE1CIiwicnVudGltZVBlcmNlbnRpbGUiOjIxLjAxLCJtZW1vcnlQZXJjZW50aWxlIjozOC4wNSwidG90YWxUZXN0cyI6MTE1MTUsInRlc3RzUGFzc2VkIjoxMTUxNX19XX0= -->

# 9. Palindrome Number

![Easy difficulty](https://img.shields.io/badge/Difficulty-Easy-137B59?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/palindrome-number/submissions/2201569192/) | 18 ms (beats 21.01%) | 19.2 MB (beats 38.05%) | 11515/11515 | 2026-11-23 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[0] == '-':
            return False
        num = ''
        for i in str(x):
            num = i + num
        if int(num) == x:
            return True
        else:
            return False
```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
