class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low <= high:
            mid=(low+high)/2
            if(nums[mid]==target):
                return mid
            if(nums[mid]>nums[low]):
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif(low==mid):
                low+=1
            elif(nums[mid]<nums[high]):
                if nums[high]>=target>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
            elif(high==mid):
                high-=1
        return -1 
