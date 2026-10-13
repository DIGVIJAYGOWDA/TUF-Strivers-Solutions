class Solution:
    def reverse(self, arr: list, n: int) -> None:
        i=0
        j=n-1
        while i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
        return temp