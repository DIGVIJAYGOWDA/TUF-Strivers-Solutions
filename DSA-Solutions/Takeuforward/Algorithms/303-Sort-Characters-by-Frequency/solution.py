class Solution:
    def frequencySort(self, s):
        #your code goes here
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        return sorted(freq, key=lambda ch:(-freq[ch],ch))