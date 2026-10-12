class Solution:
        def mostFrequentElement(self, nums):
            freq={}
            
            for i in nums:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
            
            max_freq=0
            res=None

            for i in freq:
                if freq[i]>max_freq:
                    max_freq=freq[i]
                    res=i
                
                elif freq[i]==max_freq and i<res:
                    res=i
                
            return res