class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        res = []
        while i<j:
            right = numbers[j]
            left = numbers[i]
            if right+left > target:
                j-=1
            elif right + left < target:
                i+=1
            else:
                res = [i+1,j+1]
                return res