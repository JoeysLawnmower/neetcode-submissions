class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = temparea = maxheight = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            left = heights[i]
            right = heights[j]

            if left < right: maxheight = left
            else: maxheight = right
            temparea = (j - i) * maxheight

            if temparea > maxarea: maxarea = temparea

            if left < right: i+=1
            else: j-=1
        return maxarea