# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        list_len = 0
        curr = head

        while curr:
            list_len += 1
            curr = curr.next
        
        middle = list_len // 2
        
        curr = head
        index = 1
        while curr and index <= middle:
            curr = curr.next
            index += 1

        return curr
        

