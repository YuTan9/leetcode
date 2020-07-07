class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""
        ptr = 0
        reachEnd = False
        try:
            pre = strs[0][0]
            reachEnd = len(strs[0]) == 1
            for string in strs:
                if string[0] != pre:
                    return ""
            ptr += 1
        except:
            return ""
        
        while reachEnd == False:
            nextChar = strs[0][ptr]
            for string in strs:
                if ptr == len(string) - 1:
                    reachEnd = True
                if ptr == len(string):
                    return pre
                if string[ptr] != nextChar:
                    return pre
            ptr += 1
            pre = pre + nextChar
        
        return pre