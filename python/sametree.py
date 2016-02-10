# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if not self.isSameTree(p.left,q.left) or not self.isSameTree(p.right,q.right):
                return False
            if p.val !=q.val or p.val !=q.val:
                return False
            return True
        elif not p and not q:
            return True
        else:
            return False
            
