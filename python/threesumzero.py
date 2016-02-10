class Solution(object):

    def threeSum(self, nums):

        """

        :type nums: List[int]

        :rtype: List[List[int]]

        """

        l=[]

        d={}

        nums.sort()

        for i,val in enumerate(nums):

            j=i+1

            k=len(nums)-1

            while j<k:

                sumval=val+nums[j]+nums[k]

                if(sumval==0):

                    temp=[val,nums[j],nums[k]]

                    if temp not in l: 

                        l.append(temp)

                    j+=1

                    k=k-1

                elif(sumval<0):

                    j+=1

                else:

                    k=k-1



        return l
