# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):

    def helper(self,root,path,paths):

        if not root:

            return

        if(root.left == None and root.right== None):

            path.append(str(root.val))

            x=reduce(lambda x,y: "->".join([x,y]),path)

            paths.append(x)

        else:

            self.helper(root.left,path+[str(root.val)],paths)

            self.helper(root.right,path+[str(root.val)],paths)

        

        

    def binaryTreePaths(self, root):

        """

        :type root: TreeNode

        :rtype: List[str]

        """

        paths=[]

        self.helper(root,[],paths)

        return paths

        


