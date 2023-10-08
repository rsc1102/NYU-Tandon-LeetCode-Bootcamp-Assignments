# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
```
# [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l,r = 0,len(height) -1
        while l<r:
            max_water = max(max_water, min(height[l],height[r]) * (r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return max_water
```
# [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        l,r = 0,0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r+1)>= k:
                ans.append(nums[queue[0]])
                l+=1
            r+=1
        return ans
        
```
