#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, iValue in enumerate(nums):
            # if iValue <= target:
                pair = int(target) - int(iValue)
                if pair in nums:
                    index = nums.index(pair)
                    if(index != i): 
                        return (i, index)
        
                    

