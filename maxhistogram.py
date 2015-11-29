class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        [0,2,1,5,6,2,3,0]
        [0,2,3]
        maxarea-6
        st-[0,2]
        """
        # height.insert(0,0)
        # height.append(0)
        st=[]
        maxarea=float('-inf')
        temp=0#st.append(0)
        
        for i in xrange(len(height)):
            if st:
                top=st[-1]
            while(st and height[i]<height[top]):
                st.pop()
                if st:
                    maxarea=max(maxarea,height[top]*(i-st[-1]-1))
                    top=st[-1]
                else:
                    maxarea=max(maxarea,height[top]*i)
                
            st.append(i)
            temp=i
        temp+=1
        while(st):
            top=st.pop()
            if st:
                maxarea=max(maxarea,height[top]*(temp-st[-1]-1))
            else:
                maxarea=max(maxarea,height[top]*temp)
        # height.pop(0)
        # height.pop()
        if maxarea==float("-inf"):
            return 0
        return maxarea
        
