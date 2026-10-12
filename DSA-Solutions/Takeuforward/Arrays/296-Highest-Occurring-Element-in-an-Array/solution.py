class Solution:
        def mostFrequentElement(self, nums):
            freq={}
            
            for i in nums:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1