# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        fast = head
        slow = head

        #find middle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 
        
        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(max_sum, (first.val + second.val))
            first = first.next
            second = second.next

        return max_sum
        