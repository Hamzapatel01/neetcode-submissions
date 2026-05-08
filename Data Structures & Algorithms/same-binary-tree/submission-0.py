# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we can do one of the three traversals here and check the roots
        def same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            return same(p.right,q.right) and same(p.left,q.left)

        return same(p,q)
