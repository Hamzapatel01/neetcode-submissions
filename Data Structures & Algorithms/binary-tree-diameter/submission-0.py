# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #calucalte the height of the left and right subtree and add them to 
        #get the diameter and we should take the longest height to get max dia
        res = 0
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal res
            res = max(res,left + right)
            return 1+max(left,right)
        dfs(root)
        return res