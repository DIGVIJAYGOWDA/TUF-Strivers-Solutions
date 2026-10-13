class Solution:    
    def palindromeCheck(self, s):
        return s ==''.join(reversed(s))