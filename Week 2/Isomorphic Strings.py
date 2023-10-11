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
