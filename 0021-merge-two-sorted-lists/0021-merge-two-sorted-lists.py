# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# neetcode Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the dummy node hold the result list in its self.next
        dummy = ListNode()
        # tail and dummy point to same list object
        # so, in the first iteration: tail.next and dummny.next updated to its first value, but
        # after the tail = tail.next. tail is no longer point to the same list object as dummy
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                # set next of tail to list1
                tail.next = list1
                # move list1 to next node
                list1 = list1.next
            elif list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            # move tail pointer to next node
            tail = tail.next
        
        # because the length of list1 and list2 may be different
        # after the loop we must check if there are still nodes left in either list1 or list2
        # then append them to tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next 
