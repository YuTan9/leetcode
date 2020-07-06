"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 1, 2, 3, 5. 
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l2 = [1] # no. that have never multiplied by 2
        l3 = [1] # no. that have never multiplied by 3
        l5 = [1] # no. that have never multiplied by 5
        ugly = 1
        
        for i in range(1, n):
            ugly = min(l2[0] * 2, l3[0] * 3, l5[0] * 5)
            l2 = l2 + [ugly]
            l3 = l3 + [ugly]
            l5 = l5 + [ugly]
            if(ugly == l2[0] * 2):
                l2 = l2[1:]
            if(ugly == l3[0] * 3):
                l3 = l3[1:]
            if(ugly == l5[0] * 5):
                l5 = l5[1:]
        return ugly


"""
+------------Better Solution---------------------------------------+
| Instead of using 3 lists to keep the ugly numbers that haven't   |
| been multiplied by 2, 3, or 5, use an ugly no. list, which       |
| stores all the ugly no. (since max(n)=1690), and three integers, | 
| which stores the spot that 2, 3, or 5 last multiplied            |
+------------------------------------------------------------------+

class Solution(object):
    def nthUglyNumber(self, n):
        res = [1]
        i_2, i_3, i_5 = 0, 0, 0
        for i in range(1, n):
            num = min(res[i_2]*2, res[i_3]*3, res[i_5]*5)
            if num == res[i_2] * 2:
                i_2 += 1
            if num == res[i_3] * 3:
                i_3 += 1
            if num == res[i_5] * 5:
                i_5 += 1
            res.append(num)
        return res[-1]
"""