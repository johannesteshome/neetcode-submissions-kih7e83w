class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        Max = float("-inf")

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h

            Max = max(Max, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return Max