class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while(nums[low]>nums[high]):
            if high-low <=1:
                return nums[high]
            mid=(low+high)/2
            if nums[mid]>nums[low]:
                low=mid
            elif nums[mid]<nums[high]:
                high=mid
        return nums[low]
        
