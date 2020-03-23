class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Islands = 0
        rows = len(grid)
        columns = len(grid[0])
        
        def checksurroundings(i,j):
            if ( i >= 0 and i < rows and j >=0 and j < columns and grid[i][j] == '1'):
                grid[i][j] = '0'
                checksurroundings(i+1,j)
                checksurroundings(i,j+1)
                checksurroundings(i,j-1)
                checksurroundings(i-1,j)
                
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j] == '1':
                    Islands += 1
                    checksurroundings(i,j)
        
        return Islands