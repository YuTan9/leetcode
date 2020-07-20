class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)>=len(b):
            b = '0'*(len(a)-len(b)) + b
        else:
            a = '0'*(len(b)-len(a)) + a
        
        c = zip(list(a), list(b))
        carry = 0
        sum = ''
        for x, y in reversed(c):
            if int(x) + int(y) == 0:
                if carry == 0:
                    sum = '0' + sum
                else:
                    sum = '1' + sum
                    carry = 0
            elif int(x) + int(y) == 1:
                if carry == 0:
                    sum = '1' + sum
                else:
                    sum = '0' + sum
                    carry = 1
            else:
                if carry == 0:
                    sum = '0' + sum
                    carry = 1
                else:
                    sum = '1' + sum
        if carry == 1:
            sum = '1' + sum
        return sum




"""
# wasted resource on computing 0 + the longer number
# added 0 in front of the shorter number, but that wastes resource
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        c = 0

        i = 1
        while i <= min(len(a), len(b)) or c:
            tmp = c
            if i <= len(a): 
                tmp += int(a[-i])
            if i <= len(b): 
                tmp += int(b[-i])
            
            result.append('0' if tmp % 2 == 0 else '1')
            c = 1 if tmp > 1 else 0
            i += 1
        
        # adding rest of binary number if loop didn't go through all
        result.extend(a[:-i+1][::-1])
        result.extend(b[:-i+1][::-1])
        return "".join(result[::-1])
"""