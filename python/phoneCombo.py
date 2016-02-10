class Solution(object):
    
    def getCombo(self,phonelist,curr,oneoutput,output,n,digits):
        if curr==n:
            if oneoutput:
                output.append(oneoutput)
            return 
        for x in phonelist[int(digits[curr])]:
            temp=oneoutput+x
            self.getCombo(phonelist,curr+1,temp,output,n,digits)
            
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
                abc
                def
        23
        ad 
        
        
        """
        phonelist = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n=len(digits)
        output=[]
        self.getCombo(phonelist,0,"",output,n,digits)
        return output
    
