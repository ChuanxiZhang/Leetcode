class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)
        res = [-1, -1]
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > target:
                high = mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] == target:
                res = [mid, mid]
                left = mid - 1
                right = mid + 1
                while left >= 0:
                    if nums[left] == target:
                        res[0] = left
                        left -= 1
                    else:
                        break
                while right < len(nums):
                    if nums[right] == target:
                        res[1] = right
                        right += 1
                    else:
                        break
                break
        return res

