# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not q and not p: 
            return True
        if not q or not p: 
            return False
        if p.val != q.val: 
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
            
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        