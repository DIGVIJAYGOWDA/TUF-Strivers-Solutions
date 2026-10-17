class Solution:    
    def anagramStrings(self, s, t):
        if len(s)!=len(t):
            return False

        return sorted(s)==sorted(t)