class Solution:
    def largeOddNum(self, s: str) -> str:
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2!=0:
                return s[:i+1].lstrip('0')
        return ""