class Solution:
    def pattern16(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(chr(64+i),end="")
            print()