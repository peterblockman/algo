# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the fast pointer go twice as fast as the slow pointer
        # by the time the fast pointer reach the end of the list
        # the slow pointer will reach the middle of it
        fast, slow = head, head

        # make sure that fast.next exists because we don't want fast to move
        # to the last node because we move it 2 times faster than the slow
        # pointer 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow