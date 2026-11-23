<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoibWluLXN0YWNrIiwicHJvYmxlbSI6eyJ0aXRsZSI6Ik1pbiBTdGFjayIsImZyb250ZW5kSWQiOiIxNTUiLCJkaWZmaWN1bHR5IjoiTWVkaXVtIiwidG9waWNzIjpbXX0sInJvd3MiOlt7ImlkIjoiMjIwMjIzMTcyNiIsImxhbmd1YWdlIjoicHl0aG9uMyIsImFjY2VwdGVkQXQiOiIyMDI2LTExLTIzVDIzOjQzOjM0LjcxM1oiLCJzdGF0cyI6eyJydW50aW1lIjoiMjU0IG1zIiwibWVtb3J5IjoiMzEuMSBNQiIsInJ1bnRpbWVQZXJjZW50aWxlIjo1NC45OSwibWVtb3J5UGVyY2VudGlsZSI6ODMuNTIsInRvdGFsVGVzdHMiOjQ2LCJ0ZXN0c1Bhc3NlZCI6NDZ9fV19 -->

# 155. Min Stack

![Medium difficulty](https://img.shields.io/badge/Difficulty-Medium-A65E00?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/min-stack/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/min-stack/submissions/2202231726/) | 254 ms (beats 54.99%) | 31.1 MB (beats 83.52%) | 46/46 | 2026-11-23 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
        self.min_list = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_val == None:
            self.min_val = value
            self.min_list.append(self.min_val)
        elif value <= self.min_val:
            self.min_val = value
            self.min_list.append(self.min_val)

    def pop(self) -> None:
        if self.min_val == self.stack[-1]:
            self.min_list.pop()
            if self.min_list:
                self.min_val = self.min_list[-1]
            else:
                self.min_val = None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
