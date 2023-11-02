# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # create a distance between right and left, so that when right reach outside the list left will be at the node before the node we want to remove
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move right outside the list, so left will be at where we want
        while right:
            left = left.next
            right = right.next

        # delete the node
        left.next = left.next.next

        return dummy.next