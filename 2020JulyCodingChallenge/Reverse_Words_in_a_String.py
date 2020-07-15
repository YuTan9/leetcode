class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        reverse = ""
        
        for idx, word in enumerate(arr):
            if idx == len(arr) - 1:
                reverse = str(word) + reverse
            else:
                reverse = " " + str(word) + reverse
                
        return reverse



        """
        return " ".join(reversed(s.strip().split()))
        """