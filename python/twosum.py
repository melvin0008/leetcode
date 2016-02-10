from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=defaultdict(int)
        for no,val in enumerate(nums):
            if target-val in d:
                return (d[target-val],no+1)
            else:
                d[val]=no+1
        
        return (0,0)
