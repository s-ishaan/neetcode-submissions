# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []

        def pre_order(root, scorer):
            if not root:
                scorer.append("null")
                return None

            scorer.append(root.val)
            pre_order(root.left, scorer)
            pre_order(root.right, scorer)
            
            return scorer

        t1 = pre_order(p, t1)
        t2 = pre_order(q, t2)

        if t1 == t2:
            return True
        else:
            return False