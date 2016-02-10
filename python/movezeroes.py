class Solution(object):

    def moveZeroes(self, nums):

        """

        :type nums: List[int]

        :rtype: void Do not return anything, modify nums in-place instead.

        """

        n=len(nums)-1

        i,j=0,0

        while(i<n and j<n):

            while(i<n and nums[i]!=0):

                i+=1

            while(j<n and nums[j]==0):

                j+=1

            if i<=j:

                nums[i],nums[j]=nums[j],nums[i]

            else:

                j+=1

            
