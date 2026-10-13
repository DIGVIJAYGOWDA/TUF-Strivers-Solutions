class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq={}
        sum=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        max=0
        low=None

        for i in freq:
            if freq[i]>max:
                low=max
                max=freq[i]
            
            if freq[i]<low:
                low=freq[i]
        
        sum=low+max
        return sum