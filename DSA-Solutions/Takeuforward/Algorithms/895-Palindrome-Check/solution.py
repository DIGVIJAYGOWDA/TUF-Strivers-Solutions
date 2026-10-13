class Solution:    
    def palindromeCheck(self, s):
        i=0
        j=len(s)-1

        while i<j:
            if s[i]==s[j]:
                return bool
            i+=1
            j-=1