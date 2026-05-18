# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #take one root and check for sametree so traverse each root tree and 
        #apply sametree function
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left,q.left) and isSame(p.right,q.right)
        
        def dfs(root):
            if not root and subRoot:
                return False
            if not subRoot and root:
                return True
            if isSame(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)