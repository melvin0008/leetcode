# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



from collections import deque



class Solution(object):

    def levelOrder(self, root):

        """

        :type root: TreeNode

        :rtype: List[List[int]]

        """

        if not root:

            return []

        q=deque([(root,1)])

        levelorder=[]

        prev=0

        while q:

            node,depth=q.pop()

            if(depth!=prev):

                d=[]

                levelorder.append(d)

                prev+=1

            d.append(node.val)

            if node.left:

                q.appendleft((node.left,depth+1))

            if node.right:

                q.appendleft((node.right,depth+1))

            

        return levelorder
