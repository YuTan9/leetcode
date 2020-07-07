class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = "1"
        for i in range(1,n):
            ptr = 0
            newNum = ""
            for j in range(len(num)):
                if j == len(num) - 1:
                    if ptr == j:
                        newNum = newNum + str(1) + num[j]
                    else:
                        literal = j - ptr + 1
                        newNum = newNum + str(literal) + num[j]
                else:
                    if num[j+1] != num[j]:
                        literal = j - ptr + 1
                        newNum = newNum + str(literal) + num[j]
                        ptr = j + 1
            num = newNum

            
        return num