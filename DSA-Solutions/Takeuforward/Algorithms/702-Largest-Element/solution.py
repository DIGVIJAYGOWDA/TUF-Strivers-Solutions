class Solution:
    def largestElement(self, nums):
        nums.sort()
        return nums[len(nums)-1]