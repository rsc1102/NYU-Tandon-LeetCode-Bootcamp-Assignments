class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0]*len(grid[0]) for _ in range(len(grid))]

        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if i+1<len(grid) and j+1<len(grid[0]):
                    memo[i][j] = min(memo[i+1][j],memo[i][j+1]) + grid[i][j]
                elif i + 1 < len(grid) and j + 1 == len(grid[0]):
                    memo[i][j] = memo[i+1][j] + grid[i][j]
                elif i + 1 == len(grid) and j + 1 < len(grid[0]):
                    memo[i][j]  = memo[i][j+1] + grid[i][j]
                elif i + 1 == len(grid) and j + 1 == len(grid[0]):
                    memo[i][j] = grid[i][j]

        return memo[0][0]

        
