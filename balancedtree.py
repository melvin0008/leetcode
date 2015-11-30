# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):



    def checkheight(self,root):

        if not root:

            return 0

        l=self.checkheight(root.left)

        r=self.checkheight(root.right)

        if l==-1 or r==-1:

            return -1

        if abs(l-r)>1:

            return -1

        return max(l,r)+1

    

    def isBalanced(self, root):

        """

        :type root: TreeNode

        :rtype: bool

        """

        if self.checkheight(root)==-1:

            return False

        return True
