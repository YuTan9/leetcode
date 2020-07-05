"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
"""
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        tenCell = [0] + cells + [0]
        flag = (N-14) % 14
        
        for i in range(0, 14+flag):
            tenCell[0] = (tenCell[2]+1) % 2
            tenCell[9] = (tenCell[7]+1) % 2
            newCell = [0,0,0,0,0,0,0,0,0,0]
            
            for j in range(1, 9):
                newCell[j] = 1-(tenCell[j-1] + tenCell[j+1]) % 2
            tenCell = newCell
            
        
        
        forReturn = []
        for i in range(1,9):
            forReturn = forReturn + [tenCell[i]]
        return forReturn