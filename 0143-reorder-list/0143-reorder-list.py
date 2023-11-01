# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the sencond haft
        second = slow.next
        prev = None
        # do this split in 2 parts
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # merge
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            # insert second in the middle of first and first.next
            first.next = second
            second.next = temp1 
            # move pointers
            first = temp1
            second = temp2
