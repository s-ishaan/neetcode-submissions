# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def pre_order(curr, scorer):
            if not curr:
                scorer.append(-1)
                return None
            
            scorer.append(curr.val)
            pre_order(curr.left, scorer)
            pre_order(curr.right, scorer)

            return scorer

        t1 , t2 = [], []
        t1 = pre_order(root, t1)
        t2 = pre_order(subRoot, t2)

        for i in range(len(t1)):
            if t1[i:i+len(t2)] == t2:
                return True
            
        return False
