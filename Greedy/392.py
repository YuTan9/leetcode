class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        for i in range(len(t)):
            if s[0] == t[i]:
                s = s[1:]
            if(len(s) == 0):
                break
        
        return True if len(s) == 0 else False
        