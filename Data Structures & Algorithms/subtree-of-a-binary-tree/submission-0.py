# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subRoot):
            def dfs(node1, node2):

                if not node1 and not node2:
                    return True

                if node1 and node2 and node1.val == node2.val:
                    return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
                else:
                    return False
        
        
            return dfs(root, subRoot)
        
        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            
        
        return dfs(root) or False