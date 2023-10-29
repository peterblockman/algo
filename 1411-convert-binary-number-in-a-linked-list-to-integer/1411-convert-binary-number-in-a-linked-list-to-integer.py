# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev, curr = None, head
        bnums = []
        while curr:
            bnums.append(curr.val)
            curr = curr.next

        res = 0
        for i, bn in enumerate(reversed(bnums)):
            res += 2**i * bn
        return res