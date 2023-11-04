# [Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/description/)
```python
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = defaultdict(int)
        for item in edges:
            connections[item[0]] += 1
            connections[item[1]] += 1
        
        for key in connections:
            if connections[key] == len(connections) -1:
                return key
        return 0
```

# [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)
```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = 0
        ans = 0
        for x in s:
            if x == "(":
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    ans += 1
                    counter = 0

        
        return ans + counter
```

# [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/)
```python
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1 if nums[0] >= k else -1

        cumm = [0] * (len(nums) +1)
        for i in range(len(nums)):
            cumm[i+1] = cumm[i] + nums[i]

        ans = float('inf')
        memo = deque()
        for r in range(len(cumm)):
            while memo and cumm[r] <= cumm[memo[-1]]:
                memo.pop()
            
            while memo and cumm[r] - cumm[memo[0]] >= k:
                ans = min(ans, r - memo.popleft())

            memo.append(r)

        if ans == float('inf'): return -1
        return ans
```
