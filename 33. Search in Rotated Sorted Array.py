class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[high]:
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] > nums[high]:
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                high -= 1
        return low if nums[low] == target else -1
                    
