# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBSThelper(self,root,minimum,maximum):
        if not root:
            return True
        if root.val>= minimum or root.val<=maximum:
            return False
        return self.isValidBSThelper(root.left,min(minimum,root.val),maximum) and self.isValidBSThelper(root.right,minimum,max(maximum,root.val)) 

    def isValidBST(self, root):
        if not root:
            return True
        return self.isValidBSThelper(root,float('inf'),float('-inf'))
        
        
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     l=self.isValidBST(root.left)
    #     r=self.isValidBST(root.right)
    #     if not l or not r:
    #         return False
    #     if(root.left):
    #         if root.val<= root.left.val:
    #             return False
    #     if(root.right):
    #         if root.val>= root.right.val:
    #             return False
    #     return True
                
        
