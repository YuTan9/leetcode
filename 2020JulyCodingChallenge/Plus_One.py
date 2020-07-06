"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add1 = []
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - i - 1)
        
        num += 1
        
        add1 = list(str(num))
            
        return add1