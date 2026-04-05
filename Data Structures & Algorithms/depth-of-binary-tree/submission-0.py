# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        Max = 0

        def dfs(node, length):
            nonlocal Max
            if not node:
                return
            
            Max = max(Max, length)

            dfs(node.left, length + 1)
            dfs(node.right, length + 1)
        
        dfs(root, 1)

        return Max

        