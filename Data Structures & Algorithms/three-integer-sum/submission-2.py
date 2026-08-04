class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i-1] == n:
                continue

            
            target = -n
            i += 1
            j = len(nums)-1
            while i<j:
                left = nums[i]
                right = nums[j]
                
                if right + left < target:
                    i+=1
                elif right + left > target:
                    j-=1
                else:
                    res.append([n,left,right])
                    i+=1
                    while nums[i] == nums[i - 1] and i<j:
                        i+=1
        return res