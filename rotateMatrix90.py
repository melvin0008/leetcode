class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)-1
        layers=len(matrix)/2
        for layer in xrange(layers):
            for i in xrange(layer,length-layer):
                #top matrix[layer][i]
                #bottom matrix[length-layer][length-i]
                #left matrix[length-i][layer]
                #right matrix[i][length-layer]
                temp=matrix[layer][i]
                matrix[layer][i]=matrix[length-i][layer]
                matrix[length-i][layer]=matrix[length-layer][length-i]
                matrix[length-layer][length-i]=matrix[i][length-layer]
                matrix[i][length-layer]=temp