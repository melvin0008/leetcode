class Solution:
    # @param A : tuple of integers [3 5 2 4 8 1]
    #[3 3 2 2 2 1] [8 8 8 8 8 1]
    # @return an integer
    def maximumGap(self, A):
        i=0
        n=len(A)
        j=n-1
        maxdiff=-1
        minA=[0]*n
        maxA=[0]*n
        if(len(A)==1):      
            return 0
        minA[0]=A[0]
        maxA[j]=A[j]
        for i in xrange(1,n-1):
            minA[i]=min(minA[i-1],A[i])
        
        j=n-2
        for i in xrange(j,-1,-1):
            maxA[i]=max(maxA[i+1],A[i])
            
        i,j=0,0
        while(i<n and j<n):
            if(minA[i]<=maxA[j]):
                maxdiff=max(maxdiff,j-i)
                j+=1
            else:
                i+=1
        return maxdiff
            
                
            
            
