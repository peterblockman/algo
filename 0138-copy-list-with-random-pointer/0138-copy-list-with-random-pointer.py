"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # handl edge case None
        oldToCopy = { None: None }

        # clone the nodes into a hashmap
        # because 1 node can link to a node that the curr pointer has not reached
        curr = head
        while curr:
            copied_node = Node(curr.val)
            oldToCopy[curr] = copied_node
            curr = curr.next

        # update next and random pointers of the copied_node
        curr = head
        while curr:
            copied_node = oldToCopy[curr]
            copied_node.next = oldToCopy[curr.next]
            copied_node.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]