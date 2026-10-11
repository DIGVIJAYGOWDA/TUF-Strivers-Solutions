class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        count=0
        while n>0:
            count+=1
            n=n//10
        return count