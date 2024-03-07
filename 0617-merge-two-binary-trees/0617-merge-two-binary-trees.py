# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(t1node, t2node):
           # if t1node is none, return t2node as the result of the merge
            if not t1node:
               return t2node
             # if t1node is none, return t2node as the result of the merge
            if not t2node:
                return t1node

            merged_node = TreeNode(t1node.val + t2node.val)

            # merge left children of both trees
            merged_node.left = dfs(t1node.left, t2node.left)

            # merge right children of both trees
            merged_node.right = dfs(t1node.right, t2node.right)

            return merged_node
        
        return dfs(root1, root2)