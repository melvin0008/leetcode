
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        d=defaultdict()
        i=0
        while i<len(A):
            start=i
            s=0
            while(i<len(A) and A[i]>=0 ):
                s+=A[i]
                i+=1
            end=i-1
            i+=1
            d[start]=(end,end-start+1,s)
        m=float('-inf')
        maxstart=0
        minstart=float('inf')
        maxend=len(A)
        maxlength=float('-inf')
        for k,v in d.iteritems():
            if(v[2]>m):
                m=v[2]
                maxstart=k
                maxend=v[0]
                maxlength=v[1]
            elif(v[2]==m):
                if(v[1]>maxlength):
                    maxstart=k
                    maxend=v[0]
                elif(v[1]==maxlength):
                    if(k<minstart):
                        maxstart=k
                        maxend=v[0]
        return A[maxstart:maxend+1]
                
                
                
