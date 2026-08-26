# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root, scorer):
            if not root:
                return None

            in_order(root.left, scorer)
            scorer.append(root.val)
            in_order(root.right, scorer)

            return scorer

        t1 = []
        t1 = in_order(root, t1)
        return t1[k-1]