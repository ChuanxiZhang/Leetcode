class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            h = min(height[left], height[right])
            res = max(res, h * (right - left))
            while height[left] <= h and left < right:
                left += 1
            while height[right] <= h and left < right:
                right -= 1
        return res
