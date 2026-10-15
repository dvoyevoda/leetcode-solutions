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

