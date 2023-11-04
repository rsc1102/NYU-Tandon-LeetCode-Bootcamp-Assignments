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
            
            

        
