# [Course Schedule](https://leetcode.com/problems/course-schedule/description/)
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)

        for item in prerequisites:
            hashmap[item[0]].append(item[1])
            if item[0] in hashmap[item[1]]:
                return False
            
        def dfs(course):
            if course in self.seen or hashmap[course] == []:
                return
            if course in self.stack:
                self.ans = False
                return
            
            self.stack.add(course)
            for preq in hashmap[course]:
                dfs(preq)
            self.stack.remove(course)
            self.seen.add(course)

        self.ans = True
        self.seen = set()
        for i in range(numCourses):
            self.stack = set()
            dfs(i)
            if self.ans == False:
                return False

        return self.ans 
```

# [Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
```python
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
```

# [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.k = k

        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            self.k -= 1
            if self.k >= 0:
                self.ans = root.val
            dfs(root.right)

        dfs(root) 
        return self.ans
```
