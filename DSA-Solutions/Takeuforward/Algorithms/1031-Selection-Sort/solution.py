class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(i+1):
                min_index=i
                if nums[j]<nums[i]:
                    min_index=j
                temp=nums[min_index]
                nums[min_index]=nums[j]
                nums[j]=temp
        return nums