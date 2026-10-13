class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq={}
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        max_freq=0
        low=float('inf')

        for i in freq:
            if freq[i]>max_freq:
                
                max_freq=freq[i]
            
            if freq[i]<low:
                low=freq[i]

           
                
        
        
        return max_freq+low