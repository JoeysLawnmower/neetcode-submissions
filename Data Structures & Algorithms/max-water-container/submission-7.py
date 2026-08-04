class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = temparea = maxheight = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            left = heights[i]
            right = heights[j]

            maxheight = min(heights[i], heights[j])
            width = j - i
            maxarea = max(maxarea, maxheight * width)


            if left < right: i+=1
            else: j-=1
        return maxarea