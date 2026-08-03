class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        pre = post = 1
        lis = [1] * len(nums)
        while i < len(nums) - 1:
            pre *= nums[i]
            i+=1
            lis[i] = pre
        
        while j > 0:
            post *= nums[j]
            j-=1
            lis[j]*=post
        return lis

        