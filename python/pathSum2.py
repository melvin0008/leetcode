# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSumHelper(self, root, total,path,result):
        if root==None:
            return 
        if root.left==None and root.right==None:
            if total==root.val:
                path=path+[root.val]
                result.append(path)
        self.pathSumHelper(root.left,total-root.val,path+[root.val],result)
        self.pathSumHelper(root.right,total-root.val,path+[root.val],result)
        
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        self.pathSumHelper(root,sum,[],result)
        return result
        
        