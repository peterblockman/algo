# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        comp = []
        def dfs(root1, root2):
            # base case: if both trees are empty, they are the same
            if not root1 and not root2:
                return True

            # if either of the trees are empty, they are not the same
            if not root1 or not root2:
                return False
            
            # if the vals of them are not the same, they are not the same
            if root1.val != root2.val:
                return False

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            
        return  dfs(p, q)
