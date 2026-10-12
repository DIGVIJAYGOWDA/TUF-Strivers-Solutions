class Solution:
    def secondMostFrequentElement(self, nums):
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        max_freq=0
        second_max_freq=0
       

        for i in freq:
            if freq[i]>max_freq:
                max_freq=freq[i]
                second_max_freq=max_freq
                
            elif freq[i]<max_freq and freq[i]>second_max_freq:
                second_max_freq=freq[i]
                res=i
        if second_max_freq==0:
            return -1

        res=None

        for i in freq:
            if freq[i]==second_max_freq:
                if res is None or i<res:
                    res=i

          
        return res