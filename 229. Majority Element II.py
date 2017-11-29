class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        times = len(nums) / 3
        dic = dict(collections.Counter(nums))
        return [key for key, val in dic.items() if val > times]
        
