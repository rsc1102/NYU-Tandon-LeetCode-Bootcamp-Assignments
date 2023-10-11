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
