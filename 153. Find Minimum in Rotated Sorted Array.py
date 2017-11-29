class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_num = nums[0]
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            #print low, high, mid
            if nums[mid] < min_num:
                min_num = nums[mid]
            if nums[mid] < nums[high]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return min(nums[low], min_num)
                
