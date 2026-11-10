class Solution:

    def merge(self, left, right):

        i, j = 0, 0
        result = []
        n=len(left)
        m=len(right)

        while i < n and j < m:

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        while i < n:
            result.append(left[i])
            i += 1

        while j < m:
            result.append(right[j])
            j += 1

        return result

    def mergeSort(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_arr = nums[:mid]
        right_arr = nums[mid:]

        left = self.mergeSort(left_arr)
        right = self.mergeSort(right_arr)

        return self.merge(left, right)