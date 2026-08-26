# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.n = 0
        self.max_val = -101
        def dfs(root, max_val):

            if not root:
                return None
            
            if root.val >= max_val:
                max_val = root.val
                self.n += 1
                
            dfs(root.left,max_val)
            dfs(root.right,max_val)
        

        dfs(root, self.max_val)
        return self.n