# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = deque()
        ans = []
        q.append(root)

        while q:
            lvl = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                lvl.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(lvl[-1])

        return ans