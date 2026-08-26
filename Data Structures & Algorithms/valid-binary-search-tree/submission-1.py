# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(root, lower, upper):
            if not root:
                return True

            if lower<root.val<upper:
                left = checker(root.left, lower, root.val)
                right = checker(root.right, root.val, upper)
            else:
                return False
            
            return left and right

        return checker(root, float('-inf'), float('inf'))
        