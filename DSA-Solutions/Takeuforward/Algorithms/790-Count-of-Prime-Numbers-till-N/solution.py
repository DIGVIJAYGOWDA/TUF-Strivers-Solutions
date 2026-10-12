class Solution:
    def primeUptoN(self, n):
        count=0
        
        for num in range(1,n+1):
            if n<=1:
                return 0
            divisors=0    
            for i in range(1,num+1):
                if num%i==0:
                    divisors+=1
            if divisors==2:
                count+=1
        return count