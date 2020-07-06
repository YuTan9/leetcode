class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # This method takes O(n^2) time while most of the sorting
        # algorithms can do better than that.
        # if len(t) != len(s):
        #     return False
        # for i in range(len(t)):
        #     for j in range(len(s)):
        #         if t[i] == s[j]:
        #             if j == 0:
        #                 s = s[1:]
        #             elif j == len(s) - 1:
        #                 s = s[:-1]
        #             else:
        #                 s = s[0:j] + s[j+1:]
        #             break
        
        # return True if len(s) == 0 else False

        if len(t) != len(s):
            return False
        
        s_arr = list(s)
        t_arr = list(t)
        s_arr.sort()
        t_arr.sort()
        
        
        return True if s_arr == t_arr else False