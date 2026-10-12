class Solution:
    def isPrime(self, n):
        #your code goes here
        if n<=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
            
        return True