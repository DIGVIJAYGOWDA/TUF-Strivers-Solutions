class Solution:
    def LCM(self, n1, n2):
        gcd=1
        lcm=1
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                gcd=i
                lcm=((n1*n2)/gcd)
                result=int(lcm)
        return result