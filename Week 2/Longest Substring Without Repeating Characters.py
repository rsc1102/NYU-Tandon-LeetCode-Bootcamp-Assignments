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
