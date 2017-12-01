class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {0: -1}
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                nums[i] = -1

        sum_num = 0
        res = 0

        for i in range(l):
            sum_num += nums[i]
            if sum_num in ht:
                res = max(res, i - ht[sum_num])
            else:
                ht[sum_num] = i
        return res

 
