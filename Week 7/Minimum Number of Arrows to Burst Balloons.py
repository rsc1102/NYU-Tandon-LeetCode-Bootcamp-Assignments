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
