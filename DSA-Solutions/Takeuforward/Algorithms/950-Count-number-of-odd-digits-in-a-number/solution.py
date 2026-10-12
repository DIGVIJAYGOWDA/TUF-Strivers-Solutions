class Solution:
    def countOddDigit(self, n):
        if n==1:
            return 1
        count=0
        while n>0:
            if n%2!=0:
                count=count+1
            n=n//10
        return count