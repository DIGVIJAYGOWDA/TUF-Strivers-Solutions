class Solution:
        def mostFrequentElement(self, nums):
            freq={}
            count=0
            for i in nums:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
            
            max_freq=0
            res=0
            for i in freq:

                if freq[i]>max_freq:
                    max_freq=freq[i]
                    res=i
            
                if freq[i]==max_freq and i<res:
                    res=i
            return res