class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ht = {0:-1}
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            if not k == 0:
                sum_nums %= k
            if sum_nums in ht.keys():
                if i - ht[sum_nums] > 1:
                    return True
            else:
                ht[sum_nums] = i
        return False
