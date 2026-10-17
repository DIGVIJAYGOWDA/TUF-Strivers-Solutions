class Solution:
    def arraySum(self, nums):
        #your code goes here
        if len(nums)==0:
            return 0

        if len(nums)==1:
            return nums[0]
        else:
           return nums[0]+self.arraySum(nums[1:])