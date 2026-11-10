class Solution:
    def partition(self,nums,low,high):
        pivot=nums[low]
        i=low
        j=high
        while i<j:
            while i<=high-1 and nums[i]<=pivot:
                i+=1
            while j>=low+1 and nums[j]>pivot:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
        return j


    def quickSort_Helper(self, nums, low, high):
        if low<high:
            p_index=self.partition(nums,low,high)
            self.quickSort_Helper(nums,low,p_index-1)
            self.quickSort_Helper(nums,p_index+1,high)
    
    def quickSort(self,nums):
        self.quickSort_Helper(nums,0,len(nums)-1)
        return nums