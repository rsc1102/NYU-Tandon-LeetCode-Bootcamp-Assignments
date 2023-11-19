class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = defaultdict(int)

        def dp(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i == m or j == n:
                return 0
            
            if (i,j) not in self.memo:
                self.memo[(i,j)] = dp(i+1,j) + dp(i,j+1)
            
            return self.memo[(i,j)]

        return dp(0,0)
        
