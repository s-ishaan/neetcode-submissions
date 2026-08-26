# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root,ans):
            if not root:
                return None
            
            in_order(root.left,ans)
            ans.append(root.val)
            in_order(root.right, ans)

            return ans

        ans = []
        ans = in_order(root, ans)
        return ans[k-1]