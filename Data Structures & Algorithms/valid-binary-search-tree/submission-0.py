class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(root, lower_bound, upper_bound):
            if not root:
                return True

            if lower_bound<root.val<upper_bound:
                pass
            else:
                return False
            
            left = checker(root.left, lower_bound, root.val)
            right = checker(root.right, root.val, upper_bound)

            return left and right

        return checker(root, float('-inf'), float('inf'))
            