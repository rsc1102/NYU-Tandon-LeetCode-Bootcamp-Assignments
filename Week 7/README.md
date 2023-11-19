# [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/)
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j]  = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        return dp[0][0] 
```

# [Unique Paths](https://leetcode.com/problems/unique-paths/description/)
```python
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
        
```

# [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        ans = 0
        ballonend = -float('inf')

        for x in points:
            if x[0] > ballonend:
                ans += 1
                ballonend = x[1]
        return ans
```
