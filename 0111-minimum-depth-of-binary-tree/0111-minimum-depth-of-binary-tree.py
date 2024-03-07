# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth(node):
            # base case 1: if a node emptry node, does not increase depth
            if not node:
                return 0
            # base case 2: if left child node is empty, count the right childnode
            if not node.left:
                return 1 + min_depth(node.right)
            # base case 3: if right child node is empty, count left child node
            if not node.right:
                return 1 + min_depth(node.left)

            return 1 + min(min_depth(node.left), min_depth(node.right))
        
        
        return min_depth(root)
    
