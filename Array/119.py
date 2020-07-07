class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1,1] + [0] * (rowIndex - 1)
            
            while row[-1] != 1:
                tmp = list(row)
                for i in range(1, len(tmp)):
                    if tmp[i] != 0:
                        row[i] = tmp[i] + tmp[i-1]
                    else:
                        row[i] = 1
                        break
            return row