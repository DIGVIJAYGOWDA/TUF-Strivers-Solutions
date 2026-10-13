j=len(s)-1
        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        #your code goes here
        i=0
    def reverseString(self, s):