class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        maxi = 0
        
        for n in h:
            if (n-1) not in h:
                count = 0
                while (n+count) in h:
                    count+=1
                maxi = max(count,maxi)
        return maxi

