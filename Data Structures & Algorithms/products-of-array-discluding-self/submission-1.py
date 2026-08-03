class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis = [1] * len(nums)
        pre = post = 1
        for i in range(len(nums)):
            lis[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            lis[i] *= post
            post *= nums[i]
        return lis

        