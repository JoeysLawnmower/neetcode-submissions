class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hama = {}
        for i, j in enumerate(nums):
            des = target - j
            if des in hama:
                return [hama[des], i]
                
            hama[j] = i


