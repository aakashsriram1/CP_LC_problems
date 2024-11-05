# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        
        q = []
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        