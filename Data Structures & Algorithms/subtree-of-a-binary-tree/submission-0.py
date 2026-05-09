# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #traverse both trees and compare values from the point where each root meets
        #but for that i need to track which of the node of the big tree matches the subtree
        #is it keep looping until one of the root matches?
        #if you find a matching root then you checck the subtree

        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if isSameTree(node,subRoot):
                return True
            return left or right
        return dfs(root)
