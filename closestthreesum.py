class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        minimum=float('inf')
        ret=0
        for i,x in enumerate(nums):
            j=i+1
            k=length-1
            while(j<k):
                s=x+nums[j]+nums[k]
                if abs(target-s)<minimum:
                    minimum=abs(target-s)
                    ret=s
                if s==target:
                    return s
                elif s<target:
                    j+=1
                else:
                    k-=1
        return ret
            
                    
                
