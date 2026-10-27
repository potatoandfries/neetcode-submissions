# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node: TreeNode) -> int:

            # this is to prevent infinite recursion
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(0,max_gain(node.right))

            # maximum value that can be obtained by including the current node in the path.
            price_newpath = node.val + left_gain + right_gain
            # Updated Max Sum value. 
            self.max_sum = max(self.max_sum, price_newpath)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum