# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree, subTree):
            # if we reach the end of both tree, they are the same until this point
            if not tree and not subTree:
                return True
            
            # if either of the tree empty, they are not the same
            if not tree or not subTree:
                return False
            
            # if the vals are not equal, they are not the same
            if tree.val != subTree.val:
                return False

            return isSameTree(tree.left, subTree.left) and isSameTree(tree.right, subTree.right)
        
        if not root:
            return False

        # we need to check if subRoot is a sub tree of root.left or root.right
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)