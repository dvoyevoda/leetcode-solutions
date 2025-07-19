# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findGreatestCommonDivisor(self, num1, num2):
        while num2 > 0:
            remainder = num1 % num2
            if remainder == 0:
                return num2
            num1, num2 = num2, remainder
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            next_node = current.next
            num1 = current.val
            num2 = next_node.val
            GCD = self.findGreatestCommonDivisor(num1,num2)
            current.next = ListNode(GCD, next_node)
            current = next_node
        return head