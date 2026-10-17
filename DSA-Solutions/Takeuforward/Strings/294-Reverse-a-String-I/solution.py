class Solution:
    def reverseString(self, s):
        if len(s) <= 1:
            return s

        output = self.reverseString(s[1:])
        return output + [s[0]]