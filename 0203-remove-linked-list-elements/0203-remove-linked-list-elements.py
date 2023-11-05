# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # this uses to place the slow pointer 1 node behind the fast pointer
        dummy = ListNode(0, head)
        fast, slow = head, dummy

        while fast and slow.next:
            if fast.val == val:
                slow.next = slow.next.next
                # we have to move fast because now slow and fast point to same node, so the fast pointer will be 1 node head
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next