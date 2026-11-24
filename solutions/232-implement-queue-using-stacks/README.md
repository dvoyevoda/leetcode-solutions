<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoiaW1wbGVtZW50LXF1ZXVlLXVzaW5nLXN0YWNrcyIsInByb2JsZW0iOnsidGl0bGUiOiJJbXBsZW1lbnQgUXVldWUgdXNpbmcgU3RhY2tzIiwiZnJvbnRlbmRJZCI6IjIzMiIsImRpZmZpY3VsdHkiOiJFYXN5IiwidG9waWNzIjpbXX0sInJvd3MiOlt7ImlkIjoiMjIwMjg1ODk0OSIsImxhbmd1YWdlIjoicHl0aG9uMyIsImFjY2VwdGVkQXQiOiIyMDI2LTExLTI0VDIxOjE3OjE1LjkwOVoiLCJzdGF0cyI6eyJydW50aW1lIjoiMCBtcyIsIm1lbW9yeSI6IjE5LjUgTUIiLCJydW50aW1lUGVyY2VudGlsZSI6MTAwLCJtZW1vcnlQZXJjZW50aWxlIjo3LjM1LCJ0b3RhbFRlc3RzIjoyMywidGVzdHNQYXNzZWQiOjIzfX1dfQ== -->

# 232. Implement Queue using Stacks

![Easy difficulty](https://img.shields.io/badge/Difficulty-Easy-137B59?labelColor=35383D)

[View on LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/implement-queue-using-stacks/submissions/2202858949/) | 0 ms (beats 100%) | 19.5 MB (beats 7.35%) | 23/23 | 2026-11-24 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
