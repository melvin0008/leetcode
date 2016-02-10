class Solution(object):
    def trap(self, height):
        """[0,1,0,2,1,0,1,3,2,1,2,1]
           [0,1,1,2,2,2,2,3,3,3,3,3]
           [3,3,3,3,3,3,3,3,2,2,2,1]
            0+0+1+0+1+2+1+0+0+1+0+0
        :type height: List[int]
        :rtype: int
        """
        water=0
        n=len(height)
        if n<2:
            return 0 
        l=[0]*n
        r=[0]*n
        l[0]=height[0]
        r[n-1]=height[n-1]
        for i in xrange(1,n):
          l[i]=max(l[i-1],height[i])
        for i in xrange(n-2,-1,-1):
          r[i]=max(r[i+1],height[i])
        for i, val in enumerate(height):
            m=min(l[i],r[i])
            if m> val:
                water+=m-val
            
        return water
        
