<!-- leetgit:generated -->
<!-- leetgit:state eyJzbHVnIjoicmV2ZXJzZS1saW5rZWQtbGlzdC1paSIsInByb2JsZW0iOnsidGl0bGUiOiJSZXZlcnNlIExpbmtlZCBMaXN0IElJIiwiZnJvbnRlbmRJZCI6IjkyIiwiZGlmZmljdWx0eSI6Ik1lZGl1bSIsInRvcGljcyI6W119LCJyb3dzIjpbeyJpZCI6IjIyMDE1MzkxMTUiLCJsYW5ndWFnZSI6InB5dGhvbjMiLCJhY2NlcHRlZEF0IjoiMjAyNi0xMS0yMlQyMjowNjoyNS42MThaIiwic3RhdHMiOnsicnVudGltZSI6IjAgbXMiLCJtZW1vcnkiOiIxOS4xIE1CIiwicnVudGltZVBlcmNlbnRpbGUiOjEwMCwibWVtb3J5UGVyY2VudGlsZSI6OTAuNDcsInRvdGFsVGVzdHMiOjQ0LCJ0ZXN0c1Bhc3NlZCI6NDR9fV19 -->

# 92. Reverse Linked List II

**Medium**

## Problem

[Read the problem on LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)

## Submission results

| Language | Verdict | Runtime | Memory | Tests passed | Date (UTC) |
| --- | --- | ---: | ---: | ---: | --- |
| [Python 3](python3.py) | [Accepted](https://leetcode.com/problems/reverse-linked-list-ii/submissions/2201539115/) | 0 ms (beats 100%) | 19.1 MB (beats 90.47%) | 44/44 | 2026-11-22 |

## Solution · Python 3

[View source](python3.py)

<!-- leetgit:preview -->
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        position = 1
        before_left = dummy
        left_bound = head

        # obtain left
        while left_bound and position < left:
            before_left = left_bound
            left_bound = left_bound.next
            position += 1
        
        # obtain right
        right_bound = left_bound
        while right_bound and position < right:
            right_bound = right_bound.next
            position += 1
        
        # save boundry after right node
        after_right = None
        if right_bound:
            after_right = right_bound.next

        # reverse until right
        prev = None
        curr = left_bound
        while curr and curr != after_right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 
        
        # Reconnect
        before_left.next = prev
        left_bound.next = after_right

        return dummy.next

```
<!-- /leetgit:preview -->

<!-- /leetgit:generated -->
