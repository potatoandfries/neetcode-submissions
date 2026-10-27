# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #class Solution: if not p and not q: is checking if both p and q are None. Here's what's happening:

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        # this is the example of recursion**
        ## now check left tree and right tree with same logic*
        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))
