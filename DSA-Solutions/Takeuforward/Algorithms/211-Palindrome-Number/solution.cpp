class Solution:
    def isPalindrome(self, n):
        sum=0
        rev=0
        original=n
        while n>0:
            sum=n%10
            rev=rev*10+sum
            n=n//10
        
        if rev==original:
            return bool