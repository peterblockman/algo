# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            t_next = curr.next
            # set next to prev
            curr.next = prev
            # move the two pointers forward
            prev = curr
            curr = t_next

        # at this point curr is None so return prev
        return prev