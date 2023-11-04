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
        
