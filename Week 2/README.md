# [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for x,y in zip(s,t):
            if x not in d:
                d[x] = y
            elif d[x] != y:
                return False

            if y not in e:
                e[y] = x
            elif e[y] != x:
                return False
        return True
```
# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = set()
        seen.add(s[0])
        l=0
        r = 1
        max_length = 0
        while r<len(s):
            while s[r] in seen and l<r:
                seen.remove(s[l])
                l+=1
            max_length = max(max_length,r-l+1)
            seen.add(s[r])
            r+=1
        return max_length
```
# [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)
```python
class Solution:
    def is_subset(self,s_counter,t_counter):
        for x in t_counter:
            if t_counter[x] > s_counter[x]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        t_counter = Counter(t)
        s_counter = Counter()

        l,r = 0,0
        
        valid = False
        ans = s
        while l<=r and r<len(s):
            s_counter[s[r]]+=1
            r+=1
            while l< len(s) and s_counter[s[l]] - 1 >= t_counter[s[l]]:
                s_counter[s[l]] -= 1
                l+=1
            if self.is_subset(s_counter,t_counter) and r-l <= len(ans):
                ans = s[l:r]
                valid = True
        
        if valid:  
            return ans
        return ""
```
