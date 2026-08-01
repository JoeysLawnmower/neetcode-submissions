class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        for i in nums:
            if i in has:
                has[i] += 1
            else:
                has[i] = 1
        
        ans = heapq.nlargest(k, has, key = has.get)


        return ans