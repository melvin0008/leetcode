class Solution(object):
    def check(self,arr):
        if len(arr)==len(set(arr)):
            return 1
        return 0
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n=len(board)
        y=[0,3,6]
        for i in range(n):
            row=[r for r in board[i] if r!='.']
            if not self.check(row):
                return False
            column=[r[i] for r in board if r[i]!='.']
            if not self.check(column):
                return False
        for i in y:
            for j in y:
                temp=[]
                for k in range(3):
                    for l in range(3):
                        if(board[k+i][l+j])!='.':
                            temp.append(board[k+i][l+j])
                if not self.check(temp):
                    return False
                        
        return True
