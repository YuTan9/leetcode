"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        newGrid = [[0] * (len(grid[0])+2) for i in range(len(grid)+2)]        
        parameter = 0  
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                newGrid[i+1][j+1] = grid[i][j]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Looking at newGrid[i+1][j+1]
                if newGrid[i+1][j+1] == 1:
                    # top
                    if newGrid[i][j+1] == 0:
                        parameter += 1
                    # down
                    if newGrid[i+2][j+1] == 0:
                        parameter += 1
                    # left
                    if newGrid[i+1][j] == 0:
                        parameter += 1
                    # right
                    if newGrid[i+1][j+2] == 0:
                        parameter += 1
                
        return parameter