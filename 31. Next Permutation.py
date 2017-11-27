class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return nums
        pos = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos = i
                break
        if not pos == 0:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[pos - 1]:
                    nums[i], nums[pos - 1] = nums[pos - 1], nums[i]
                    break

        left, right= pos, len(nums) - 1
        while left < right:
            t = nums[left]
            nums[left] = nums[right]
            nums[right] = t
            left += 1
            right -= 1


                
