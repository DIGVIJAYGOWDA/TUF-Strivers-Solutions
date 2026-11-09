class Solution:
    def bubbleSort(self, nums):
        n=len(nums)

        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        return nums