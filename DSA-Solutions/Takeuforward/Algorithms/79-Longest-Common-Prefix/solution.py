class Solution:  
    def longestCommonPrefix(self, strs):
        #your code goes here 
        res=''
        min_len=min(len(s)for s in strs)
        for i in range(min_len):
            for j in strs:
                if j[i]!=strs[0][i]:
                    return res
            res=res+strs[0][i]

        return res