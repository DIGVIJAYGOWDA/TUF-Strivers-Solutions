class Solution:
    def reverseNumber(self, n):
        rev=0
        sum=0
        while n>0:
            sum=n%10
            rev=rev*10+sum
            n=n//10
        return rev