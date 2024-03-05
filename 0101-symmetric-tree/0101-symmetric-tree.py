# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            # Base case 1: If both nodes are Empty, they are mirror
            if not left and not right:
                return True
            # Base case 2: If only one node is Empty or values are different, they are not mirror
            if not left or not right:
                return False
            # Base case 3: if values of the nodes mismatch, they are not mirror
            # if left.val != right.val:
            #     return False

            # Because it is a mirror of itself:
            # the left child node of a left node and the right child node of a right node must be the same
            # the same for right/left
            # if we use base case 3 above then we don't need to include left.val == right.val in the return statement
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        # Check if the tree is symmetric starting from the root
        if not root:
            return True
        return isMirror(root.left, root.right)