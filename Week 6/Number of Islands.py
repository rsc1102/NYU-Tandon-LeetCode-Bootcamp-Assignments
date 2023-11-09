class Solution:
    def drown_island(self,grid,i,j):
        if (i<0 or i>= len(grid) or j<0 or j>= len(grid[0])) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.drown_island(grid,i+1,j)
        self.drown_island(grid,i,j + 1)
        self.drown_island(grid,i-1,j)
        self.drown_island(grid,i,j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.drown_island(grid,i,j)
        return count
