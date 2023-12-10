# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        queue = deque([root])
        res = [[root.val]]
        
        while len(queue) > 0:
            vals = []
            size = len(queue)
            for i in range(size):
                visited_node = queue.pop()
                if visited_node.left:
                    queue.appendleft(visited_node.left)
                    vals.append(visited_node.left.val)
                if visited_node.right:
                    queue.appendleft(visited_node.right)    
                    vals.append(visited_node.right.val)

            if len(vals) > 0:
                res.append(vals)

        return res
            
            
