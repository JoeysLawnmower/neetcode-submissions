class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hama = {}
        for i in nums:
            if i in hama:
                return True
            else:
                hama[i] = 1
        return False
        