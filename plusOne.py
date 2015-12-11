class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)-1
        i=0
        j=n
        carry=1
        while(i<=j and carry==1):
                carry=0
                if digits[j]==9:
                    digits[j]=0
                    carry=1
                else:
                    digits[j]+=1
                
                j-=1
        if j<i and carry==1:
            digits.insert(0,1)
        return digits
                
