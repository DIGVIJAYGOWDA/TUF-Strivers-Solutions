class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        #your code goes here
        map_s={}
        map_t={}

        min_len=min(len(s),len(t))
        if len(s)!=len(t):
            return False
        for i in range(min_len):
            if s[i] in map_s and map_s[s[i]]!=t[i]:
                return False
            if t[i] in map_t and map_t[t[i]]!=s[i]:
                return False

            map_s[s[i]]=t[i]
            map_t[t[i]]=s[i]
            
        return True