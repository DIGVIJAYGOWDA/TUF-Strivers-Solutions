class Solution:
    def secondLargestElement(self, nums):
        nums.sort()
        j=len(nums)-1
        while j>0:
            if nums[j-1]<nums[j] and nums[j-1]!=nums[j]:
                return nums[j-1]
            j-=1
        return -1