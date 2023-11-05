class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for x in nums:
            counter[x]+=1

        heap = []
        for key in counter:
            heapq.heappush(heap,(-1*counter[key],key))
        
        ans = []
        while k:
            _ , key = heapq.heappop(heap)
            ans.append(key)
            k-=1
        return ans
