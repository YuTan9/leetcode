"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""



class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hd = 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                hd = hd + 1
            x = x // 2
            y = y // 2
            
        return hd