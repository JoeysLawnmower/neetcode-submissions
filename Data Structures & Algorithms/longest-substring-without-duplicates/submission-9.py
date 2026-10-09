class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hama = {}
        length = 0
        left = 0

        for right, char in enumerate(s):
            
            if char in hama and hama[char] >= left:
                left = hama[char] + 1
            
            hama[char] = right

            length = max(length, right - left + 1)
        return length