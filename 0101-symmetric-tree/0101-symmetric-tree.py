# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1, node2):
            # we reach the end, they should be symmetric
            if not node1 and not node2:
                return True
            
            # either of them is empty means they are not valid
            if not node1 or not node2:
                return False

            # diffrent values: not symmetric
            if node1.val != node2.val:
                return False
            
            # check left child of node1 and right child of node2 and vice versa
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        # passing root as both parameters
        return isMirror(root, root)
            