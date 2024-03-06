# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # level order traverse
        if not root:
            return 0
        levels = [[root.val]]
        q = deque([root])
        while len(q) > 0:
            node_nums = len(q)
            vals = []
            for i in range(node_nums):
                visited_node = q.pop()
                if visited_node.left or visited_node.right:
                    if visited_node.left:
                        q.appendleft(visited_node.left)
                        vals.append(visited_node.left.val)
                    if visited_node.right:
                        q.appendleft(visited_node.right)
                        vals.append(visited_node.right.val)
            if len(vals) > 0:
                levels.append(vals)
        return len(levels)