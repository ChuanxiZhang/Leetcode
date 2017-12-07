class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def back(nums, tmp):
            res.append(tmp)
            for i in range(len(nums)):
                back(nums[i + 1:], tmp + [nums[i]])
        back(nums, [])
        return res

                
